from transformers import pipeline 
from transformers import AutoModelForSequenceClassification 
from transformers import BertJapaneseTokenizer 
import random

# from huggingface_hub import snapshot_download
# download_path = snapshot_download(repo_id="daigo/bert-base-japanese-sentiment")

# print(download_path)
# dir_name = '/workspaces/fastapi/model'

# # パイプラインの準備
# model = AutoModelForSequenceClassification.from_pretrained(dir_name)
# tokenizer = BertJapaneseTokenizer.from_pretrained(dir_name) 

# #モデルのダウンロード
# model.save_pretrained(dir_name)
# tokenizer.save_pretrained(dir_name)

# nlp = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer) 

# マンガの台詞
# manga_list = ["“海賊王”に！！！おれはなるっ！！！！",
#               "あきらめたらそこで試合終了ですよ……？",
#               "計画通り",
#               "お前はもう 死んでいる",
#               "生殺与奪の権を他人に握らせるな！",
#               "さすがディオ！ おれたちにできない事を平然とやってのける そこにシビれる！ あこがれるゥ！",
#               "我がドイツの医学薬学は世界一ィィィ！",
#               "『てめーは、おれを怒らせた』",
#               "だが断る",
#               "吐き気をもよおす『邪悪』とはッ！ なにも知らぬ無知なる者を利用する事だ……!! 自分の利益だけのために利用する事だ… 父親がなにも知らぬ『娘』を!! てめーだけの都合でッ！ 許さねえッ！ あんたは今 再びッ！ オレの心を『裏切った』ッ！"]

# 感情分析の実行
# for manga in manga_list:
#     print(nlp(manga))

# # 感情分析の実行
# for manga in manga_list:
#     print(nlp(manga))

class NegaPosi:
    def __init__(self):
        dir_name = '/workspaces/fastapi/model'
        self.model = AutoModelForSequenceClassification.from_pretrained(dir_name)
        self.tokenizer = BertJapaneseTokenizer.from_pretrained(dir_name) 

    def reply(self, input: str):
        nlp = pipeline("sentiment-analysis", model=self.model, tokenizer=self.tokenizer) 
        negaposi = nlp(input)[0]["label"]
        if negaposi == "ネガティブ":
            rep_list = ["わかる、つらいよね", "うんうん、"]
        else:
            text = "いいね！"
        text = random.choice()
        return text