import pickle
from lib.openai_call import get_embedding

# QA 쌍이 있음 -> 해당 쌍마다 [Question | Answer | Number | Question Embedding] 으로 저장.
# 보편적인 질문에 대한 자기 얘기를 쓰면 "보편적인 질문 + 내가 작성한 답변" 과 DB의 "질문 + 답변"의 코사인 유사도 구해서 제일 높은거 3개의 answer을 context로 첨부

def store_vector(data):
    try:
        question_list = []
        answer_list = []
        qa_number = []
        question_embedding = []

        for data_index in range(len(data)):
            question = data[data_index]["Question"] # 데이터로부터 질문 파싱
            answer = data[data_index]["Answer"] # 데이터로부터 질문에 대한 대답 파싱

            question_list.append(question)
            answer_list.append(answer)
            qa_number.append(data_index + 1) # 질문-대답 (QA)의 index
            question_embedding.append(get_embedding(question + "\n\n" + answer)) # question_embedding에 질문-대답 쌍 함게 업로드

        print(len(question_list))

        paragraph_dict = {"question_list": question_list, "answer_list": answer_list, "qa_number": qa_number, "question_embedding": question_embedding}
        with open('self_introductions.pickle', 'wb') as f: # vectorDB 대신 pickle 파일로 저장
            pickle.dump(paragraph_dict, f)
        return 200

    except Exception as e:
        print(f"An error occurred: {e}")  # 오류 메시지 출력
    return 500  # 실패 시 500 반환

