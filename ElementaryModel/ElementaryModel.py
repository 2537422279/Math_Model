
import re

'''
三个系学生共200名（甲系100，乙系60，丙系40），代表会议共20席，
按比例分配，三个系分别为10，6，4席。

现因学生转系，三系人数为103, 63, 34, 问20席如何分配。


'''
class Fair_Distribution():
    abc_sum = 200
    a = 103 #甲
    b = 63 #乙
    c = 34 #丙专业
    def __init__(self):
        pass
    def proportion(self,seats):
        # 转系之后:20席分配时
        pro200_a = self.a / self.abc_sum  #席位分配时，占总人数比例
        pro200_b = self.b / self.abc_sum
        pro200_c = self.c / self.abc_sum
        proSeats_a = seats*pro200_a  #席位里面所占的比例
        proSeats_b = seats*pro200_b
        proSeats_c = seats*pro200_c
        # print(proSeats_a,proSeats_b,proSeats_c)
        pattern = '\.(\d{1})'
        results_re_a = re.findall(pattern,str(proSeats_a))[0]
        results_re_b = re.findall(pattern,str(proSeats_b))[0]
        results_re_c = re.findall(pattern,str(proSeats_c))[0]
        # print(results_re_a,results_re_b,results_re_c)

        max_re_i = max(results_re_a,results_re_b,results_re_c)
        self.results_a = int(proSeats_a)
        self.results_b = int(proSeats_b)
        self.results_c = int(proSeats_c)
        # print('按人数比例分配时（把在公平范围内能分的先分好）：',self.results_a, self.results_b, self.results_c) #初次分配结果

        results_a2 = int(proSeats_a)
        results_b2 = int(proSeats_b)
        results_c2 = int(proSeats_c)
        for i in range(0,(seats-20+1)):
            if max_re_i == results_re_a:
                results_a2 = int(proSeats_a) + 1
                max_re_i = max(results_re_b, results_re_c)
            elif max_re_i == results_re_b:
                results_b2 = int(proSeats_b) + 1
                max_re_i = max(results_re_a, results_re_c)
            else:
                results_c2 = int(proSeats_c) + 1
                max_re_i = max(results_re_a, results_re_b)

        print('比例分配时,分配{}席：'.format(seats),results_a2, results_b2, results_c2) #进行尾数比较之后的+1的分配结果

        return [self.results_a, self.results_b, self.results_c] #进行尾数比较之后的+1的分配结果
        # seats个席位的分配结果，显然20、21之间的过渡即可知道这样分配是不合理的。

    def get_Q(self,n,p):  #n为按人数比例分配时的席位,p为该方总人数
        # p1 / n1 > p2 / n2  >>对A不公平
        # 假设现在有两方来进行分配、解决这两方的分配之后，便可以扩展到n方的分配
        Q = p**2/(n*(n+1))   #动态的相对不公平度
        return Q
        #定义并计算绝对不公平度 ---一个衡量公平分配的数量指标
    def main(self):
        # 20席分配时
        s20 = fair.proportion(20)  # 10 6 3
        print(s20)
        # 21席分配时
        s21 = fair.proportion(21)  # 10 6 3
        print('\n')
        # 第20席分配时
        Q11 = fair.get_Q(s20[0],self.a)
        Q12 = fair.get_Q(s20[1],self.b)
        Q13 = fair.get_Q(s20[2],self.c)
        print('分配第20席时得相对不公平度：', Q11, Q12, Q13)
        Q = max(Q11,Q12,Q13)
        if Q == Q11:  #说明对甲系得不公平度最大，这时候应该第20席分给甲，以下同理
            self.results_a +=1
            s20[0] += 1
        elif Q==Q12:
            self.results_b += 1
            s20[1] += 1
        else:
            self.results_c +=1
            s20[2] += 1
        print("第20席得公平的分配结果：", self.results_a, self.results_b, self.results_c)

        # 第21席分配时[在分配好第20席得基础上进行分配第21席位]
        Q21 = fair.get_Q(s20[0], self.a)
        Q22 = fair.get_Q(s20[1], self.b)
        Q23 = fair.get_Q(s20[2], self.c)
        print('分配第20席时得相对不公平度：', Q21, Q22, Q23)
        Q = max(Q21, Q22, Q23)
        if Q == Q21:  # 说明对甲系得不公平度最大，这时候应该第20席分给甲，以下同理
            self.results_a += 1
        elif Q == Q22:
            self.results_b += 1
        else:
            self.results_c += 1
        print("第21席得公平的分配结果：", self.results_a, self.results_b, self.results_c)
        print("公平的分配结果：", self.results_a, self.results_b, self.results_c)





if __name__ == '__main__':
    fair = Fair_Distribution()
    fair.main()





