# from fastapi import APIRouter
# from pydantic import BaseModel

# from app.graph.graph import graph

# from app.llm.anthropic import llm

# router = APIRouter()


# class WebhookRequest(BaseModel):

#     context: str

#     question: str


# @router.post("/webhook")
# def webhook(request: WebhookRequest):

#     result = graph.invoke(
#         {
#             "context": request.context,
#             "question": request.question,
#         }
#     )
    
#     # print(f"response from graph : {result['answer']}")

#     return {
#         "answer": result["answer"]
#     }
    
    
#     # response = llm.invoke("Why do parrots talk?")
#     # return {
#     #     "answer": response.content, 
#     #     "raw" : response
#     # }