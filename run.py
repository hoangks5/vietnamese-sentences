import re
import json
from math import log

def xoadau(tu):
  tu = re.sub('[êếềệễểeéèẹẽẻ]','e',tu)
  tu = re.sub('[áàạãảăắằẳẵặâấầậẫẩ]','a',tu)
  tu = re.sub('[đ]','d',tu)
  tu = re.sub('[íìịĩỉ]','i',tu)
  tu = re.sub('[óòỏọõơớờợỡởôốồộổỗ]','o',tu)
  tu = re.sub('[úùụủũưứừựữử]','u',tu)
  tu = re.sub('[ýỳỷỹỵ]','y',tu)
  return tu

t = open('nguphapvietnam.txt','r',encoding='UTF-8')
t1 = t.read().splitlines() # đọc từng dòng
# Tạo thư viện các trường hợp khả năng có thể đánh dấu
rong = {}
for tu in t1:
  tu = tu.lower() # bỏ in hoa
  xoa_dau = xoadau(tu) # xóa dấu
  if xoa_dau not in rong: # nếu từ chưa có trong thư viện thì sẽ thêm vào
    rong[xoa_dau] = set()
  rong[xoa_dau].add(tu)

# Vi du rong['ha']
# {'ha', 'hà', 'há', 'hã', 'hạ', 'hả'}


# Tạo thư viện phân tích ngữ cảnh của 1 từ .
rong1 = {}
for tu in open('thuvientiengviettonghop.txt',encoding='UTF-8'):
  load = json.loads(tu)
  load1 = load['s']
  rong1[load1] = load 
size_rong1 = len(rong1)
zz = 0
for tu in rong1:
  zz += rong1[tu]['sum']

# Ví dụ rong1['hoàng']
# Kết quả trả về số từ đằng sau từ hoàng và số lần lặp lại


def xac_suat(sau,truoc):
    if sau not in rong1:
        return 1/zz;
    if truoc not in rong1[sau]['next']:
        return 1/(rong1[sau]['sum']+zz)
    return (rong1[sau]['next'][truoc]+1)/(rong1[sau]['sum']+zz)

# Ví dụ xác suất từ 'hoàng' đứng trước từ 'anh'
# xac_suat('hoàng','anh')

# hàm beam search tính xác suất tối ưu chọn từ
def beam_search(words1, k=3):
  sequences = []
  for idx, word in enumerate(words1):
    if idx == 0:
      sequences = [([x], 0.0) for x in rong.get(word, [word])]
    else:
      all_sequences = []
      for seq in sequences:
        for truoc in rong.get(word, [word]):
          sau = seq[0][-1]
          proba = xac_suat(sau, truoc)  
          proba = log(proba)
          new_seq = seq[0].copy()
          new_seq.append(truoc)
          all_sequences.append((new_seq, seq[1] + proba))
      all_sequences = sorted(all_sequences,key=lambda x: x[1], reverse=True)
      sequences = all_sequences[:k]
  return sequences

inp = input("Nhập vào câu không dấu: ")  # Đưa vào đoạn văn bản ko dấu

sentence = xoadau(inp)
words1 = sentence.split()
results1 = beam_search(words1, k=5)
inp = ' '.join(results1[0][0])

print(inp) # kết quả



















