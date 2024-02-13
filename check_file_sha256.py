import hashlib
 
def sha256_checksum(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            sha256.update(chunk)
    return sha256.hexdigest()

check_file_list = []
check_file_list.append("/root/autodl-tmp/models/ZhipuAI/chatglm3-6b/pytorch_model-00001-of-00007.bin")
check_file_list.append("/root/autodl-tmp/models/ZhipuAI/chatglm3-6b/pytorch_model-00002-of-00007.bin")
check_file_list.append("/root/autodl-tmp/models/ZhipuAI/chatglm3-6b/pytorch_model-00003-of-00007.bin")
check_file_list.append("/root/autodl-tmp/models/ZhipuAI/chatglm3-6b/pytorch_model-00004-of-00007.bin")
check_file_list.append("/root/autodl-tmp/models/ZhipuAI/chatglm3-6b/pytorch_model-00005-of-00007.bin")
check_file_list.append("/root/autodl-tmp/models/ZhipuAI/chatglm3-6b/pytorch_model-00006-of-00007.bin")
check_file_list.append("/root/autodl-tmp/models/ZhipuAI/chatglm3-6b/pytorch_model-00007-of-00007.bin")
check_file_list.append("/root/autodl-tmp/models/ZhipuAI/chatglm3-6b/tokenizer.model")

for file_path in check_file_list:
    checksum = sha256_checksum(file_path)
    print(f'SHA256校验值：{checksum}')