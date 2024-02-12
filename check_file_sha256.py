import hashlib
 
def sha256_checksum(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            sha256.update(chunk)
    return sha256.hexdigest()
 
file_path = "/root/autodl-tmp/models/ZhipuAI/chatglm3-6b/pytorch_model-00001-of-00007.bin"
checksum = sha256_checksum(file_path)
print(f'SHA256校验值：{checksum}')