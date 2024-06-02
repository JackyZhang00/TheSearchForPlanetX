def isPrime(number):
    result = True
    if number == 1:
        return False
    for i in range(2,number):
        if number % i == 0:
            result = False
            break
    return result

class Draft():
    def __init__(self,level,players) -> None:
        self.level = level
        self.players = players
        self.planets = {}
        self.actionList = {}
        while True:
            try:
                yourNumber = int(input("你的编号为："))
            except:
                print("编号输入有误，请重新输入")
            if yourNumber in range(1,players+1):
                self.yourNumber = yourNumber
                break
            else:
                print(f"编号超出范围，玩家人数为{players}，请输入1~{players}的整数。请重新输入，")
        allowed_levels = (12,18)
        assert level in allowed_levels, "Level Value Error"
        for i in range(1,level+1):
            self.planets[i] = ['A','D','G','X','E']
            if isPrime(i):
                self.planets[i].append('C')
        for i in range(1,players+1):
            self.actionList[i] = []
    
    def showDraftMap(self):
        result = ""
        for i in range(1,self.level//2+1):
            if isPrime(i):
                result = result + f"{i}: {self.planets[i]}\t {i+self.level//2}: {self.planets[i+self.level//2]} \n"
            else:
                result = result + f"{i}: {self.planets[i]}\t\t {i+self.level//2}: {self.planets[i+self.level//2]} \n"
        print(result)

    def deletePlanet(self,number,planet):
        assert isinstance(number,int) or isinstance(number,list), "扇区类型应当为整数或列表"
        if isinstance(number,int):
            assert number in range(1,self.level+1), f"输入扇区{number}超出范围，扇区范围应当在1~{self.level}"
            self.planets[number].remove(planet)
        if isinstance(number,list):
            for i in number:
                assert isinstance(i, int), f"扇区{i}类型错误，应当为整数"
                assert i in range(1,self.level+1), f"输入扇区{i}超出范围，扇区范围应当在1~{self.level}"
                self.planets[i].remove(planet)
    
    def assertPlanet(self,number,planet):
        assert number in range(1, self.level+1), f"输入扇区{number}超出范围，扇区范围应当在1~{self.level}"
        if not isPrime(number):
            assert not planet == 'C', f"扇区{number}内不可能存在行星{planet}"
        if planet not in self.planets[number]:
            choice = input("当前扇区内已没有该行星，是否要将其添加至扇区内？[Y]/N")
            if choice in ['N','n']:
                pass
            else:
                self.planets[number] = [planet]
        else:
            self.planets[number] = [planet]

    def addAction(self,number,action):
        assert isinstance(number,int), "玩家编号类型应当为整数"
        assert number in range(1,self.players+1), "玩家编号超出范围"
        if number == self.yourNumber:
            result = input("请输入结果：")
            self.actionList[number].append(action+":"+result)
        else:
            self.actionList[number].append(action)
    
    def showActionList(self):
        for i in range(1,self.players+1):
            print(f"{i}",end="\t")

        print("")
        len_list = [len(self.actionList[i]) for i in range(1,self.players+1)]
        # print(f"TEST : {len_list}")
        for i in range(max(len_list)):
            for j in range(1,self.players+1):
                try:
                    print(self.actionList[j][i], end="\t")
                except:
                    print("\t",end='')
            print("")


