import math
class Algorithms:

    def __init__(self):
        self.counter = 0

    def half_devide_search_ans(self,a,b,func, acc):
        # 二分法：a和b为区间起点终点，func为函数，可以自定义，acc为精度要求
        self.counter += 1
        c = (a+b)/2
        print("第" + str(self.counter) + "次迭代： "+"c: "+str(c) + "\nfa = " + str(func(a)) + " fb = " + str(
            func(b)) + " fc = " + str(func(c)))
        if(abs(b-a)<acc):
            self.counter = 0
            return c
        
        if(func(c)==0):
            self.counter = 0
            return c
        if(func(a)*func(c)<0):return self.half_devide_search_ans(a,c,func,acc)
        else:return self.half_devide_search_ans(c,b,func,acc)

    def iterate_method(self, start, func, acc):
        # 单点迭代，start为起点，func为迭代公式，acc为精度
        memory = start + 2*acc
        while(abs(memory-start)>acc):
            self.counter+=1
            memory = start
            start = func(start)
            print("第"+str(self.counter)+"次迭代： x("+str(self.counter)+") = "+str(memory)+
                  "\t\tx("+str(self.counter+1)+") = "+str(start))
        self.counter = 0
        print("最终结果： "+str(start))
        print(func(start))
        return start


if __name__ == "__main__":
    solution = Algorithms()
    # def funcx(x):
    #     return math.pow(x, 3)-2*x-5
    # c = solution.half_devide_search_ans(2,3,funcx,acc=0.005)
    # print(funcx(c))


    def funcx(x):
        return pow((1 + (x*x)),1/3)
    c = solution.iterate_method(1.5, funcx, 0.00001)
    print(c*c*c-c*c-1)
