from modelscope.msdatasets import MsDataset


ds =  MsDataset.load('chatglm_llm_fintech_raw_dataset', split='train', use_streaming=True, stream_batch_size=1, cache_dir = "/root/autodl-tmp/data/")
for item in ds:
    print(item)