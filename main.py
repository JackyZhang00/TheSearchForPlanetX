from Draft import Draft

draft = Draft(12,2)
while True: 
    allowList = [1,2,3]
    x = int(input("请输入指令：\n 1 - 查看当前草稿\n 2 - 删除候选项\n 3 - 推断扇区\n 4 - 添加行动\n 5 - 查看行动\n 0 - 退出\n : "))
    if x == 1:
        draft.showDraftMap()
    elif x == 2:
        sections = input("请输入扇区，可以使用整数如1，2；也可以使用列表形式，如[1,3,5]")
        planet = input("请输入欲删除的行星代码")
        try:
            draft.deletePlanet(eval(sections),planet.upper())
        except:
            print("输入错误，请重新输入")
    elif x == 3:
        section = input("请输入扇区，使用整数如1，2")
        planet = input("请输入行星代码")
        try:
            draft.assertPlanet(eval(section),planet.upper())
        except:
            print("输入错误，请重新输入")
    elif x == 4:
        try:
            number = int(input("请输入当前玩家编号"))
        except:
            print("编号类型错误，请重新输入")

        action = input("请输入行动")
        # draft.addAction(number,action)
        try:
            draft.addAction(number,action)
        except:
            print("输入错误，请重新输入")

    elif x == 5:
        draft.showActionList()
    elif x == 0:
        choice = input("程序将退出（不保存！），确定要退出吗？[N]/Y：")
        if choice in ['Y','y']:
            break
        else:
            pass
    else:
        print("无效代码，请重新输入")
