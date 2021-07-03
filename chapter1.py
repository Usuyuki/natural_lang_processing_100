
#00 文字列の逆順

pro0="stressed"
list_pro0=list(reversed(pro0))
reverse_chr="".join(list_pro0) #配列を任意の文字列で連結→ "->".join(["a","b"])だと→a->bの文字になる
print( reverse_chr)

#01 文字列取り出し「パタトクカシーー」
pro1="パタトクカシーー"
print(pro1[0]+pro1[2]+pro1[4]+pro1[6]) #pythonで文字の切り出しは変数[i]でOK

#02 「パトカー」＋「タクシー」＝「パタトクカシーー」
pro2_1="パトカー"
pro2_2="タクシー"
result=""

for i in range(4):
    result+=pro2_1[i]
    result+=pro2_2[i]
print(result)


#03 単語に分割して文字列を配列にする

pro3="Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."


bunkatu_3=pro3.replace(",","").replace(".","").split()

char_counter=[]

for x in bunkatu_3:
    char_counter.append(len(x))
print(char_counter)

#04 辞書型配列への登録
pro4="Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
bunkatu_4=pro4.replace(",","").replace(".","").split()

renso_4={}  #辞書型は[]ではなく{}
i=0
print(bunkatu_4)

#enumerateをforで使うとインデックス付きにできる。さらに第２引数で開始の数字も変えれる
for i,x in enumerate(bunkatu_4, 1): 
    if(i==1 or i==5 or i==6 or i==7 or i==8 or i==9 or i==15 or i==16 or i==19):
        renso_4[x[0:1]]=i
    else:
        renso_4[x[0:2]]=i
print(renso_4)


#5  N-gram

'''
N-gramとは
任意の文字列や文書を連続したn個の文字で分割するテキスト分割方法．
特に，nが1の場合をユニグラム（uni-gram），2の場合をバイグラム（bi-gram），3の場合をトライグラム（tri-gram）と呼ぶ．
'''

given_char="I am an NLPer"

def n_gram(n,list_data):
    n_gramed=[]
    length=len(list_data) +(-n+1)
    for x in range(length):
        n_gramed.append(list_data[x:x+n])
    return n_gramed


print("文字")
print(n_gram(2,given_char))
print("単語")
print(n_gram(2,given_char.split()))
