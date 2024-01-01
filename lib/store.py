import itertools
import pinecone
from lib.openai_call import get_embedding

# QA 쌍이 있음 -> 해당 쌍마다 [Question | Answer | Number | Question Embedding] 으로 저장.
# 보편적인 질문에 대한 자기 얘기를 쓰면 "보편적인 질문 + 내가 작성한 답변" 과 DB의 "질문 + 답변"의 코사인 유사도 구해서 제일 높은거 3개의 answer을 context로 첨부

def chunks(iterable, batch_size=100):
    it = iter(iterable)
    chunk = tuple(itertools.islice(it, batch_size))
    while chunk:
        yield chunk
        chunk = tuple(itertools.islice(it, batch_size))

def generate_data(datas):
    for index, data in enumerate(datas):
        question = data[0]
        answer = data[1]
        qa = question + "\n\n" + answer
        qa_embedding = get_embedding(qa)
        qa_index = index + 1
        print(qa_index)
        yield (
            str(qa_index),
            qa_embedding,
            {
                "question": question,
                "answer": answer,
                "qa_index": qa_index
            }
        )