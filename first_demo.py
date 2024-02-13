from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained("/root/autodl-tmp/models/ZhipuAI/chatglm3-6b", trust_remote_code = True)
model = AutoModel.from_pretrained("/root/autodl-tmp/models/ZhipuAI/chatglm3-6b", trust_remote_code = True, device = "cuda")
model = model.eval()
response, history = model.chat(tokenizer, "你好", history = [])
print(response)