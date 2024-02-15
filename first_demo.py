from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained("/root/autodl-tmp/models/ZhipuAI/chatglm3-6b", trust_remote_code = True)
model = AutoModel.from_pretrained("/root/autodl-tmp/models/ZhipuAI/chatglm3-6b", trust_remote_code = True, device = "cuda")
model = model.eval()
response, history = model.chat(tokenizer, "你好", history = [])
print(response)

prompt_text = "类型#裙*版型#显瘦*材质#网纱*风格#性感*裙型#百褶*裙下摆#压褶*裙长#连衣裙*裙衣门襟#拉链*裙衣门襟#套头*裙款式#拼接*裙款式#拉链*裙款式#木耳边*裙款式#抽褶*裙款式#不规则"
response, history = model.chat(tokenizer, prompt_text, history = [])
print(response)