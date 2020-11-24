file = input("Enter file name : ")
fn = open(file)
fn_list = list()
fn_dict = dict()
for i in fn:
    if i.startswith("From "):
        fn_split = i.split()
        fn_list.append(fn_split[1])
for i in fn_list:
    fn_dict[i] = fn_dict.get(i,0)+1
    #아래와 마찬가지 이다. 조금 다른점은 fn_dict.get함수인데,
    #fn_dict.get함수는 원래는 value값을 return해주는 함수이지만, default값을 설정해줄수 있어
    # 만약 i가 dict안에 없더라도 default값을 이용해서 dict안에 생성을 한다.
maxv = None
maxk = None
for i,v in fn_dict.items():
    #for 문안에는 dict에서 가지고온 items에서 두개의 변수를 loop를 돌릴수있다.
    if maxv == None:
        maxk = i #i자체가 이미 loop를 돌아가면서 key값을 받는 것으로 지정되어 있다.
        maxv = fn_dict[i]#fn_dict[]자체가 이미 value 값을 받아오는 함수.
        #그말은 즉슨 무슨말이냐 value나 key같은 함수를 사용해서 값을 갖고 오지 않아도
        #그냥 i, fn_dict[i]를 사용해서 값을 갖고올 수 있다는 말씀.
    elif maxv < fn_dict[i]:
        maxk = i
        maxv = fn_dict[i]
print(maxk,maxv)