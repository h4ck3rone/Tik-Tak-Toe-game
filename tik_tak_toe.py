template = """ --- --- ---
| 1 | 2 | 3 |
 --- --- ---
| 4 | 5 | 6 |
 --- --- ---
| 7 | 8 | 9 |
 --- --- ---
"""
victories = ['123', '456', '789', '147', '258', '369', '357', '159']
while True:
    branch = input("-------------------------------\n"
                   "1 -> New Game\n"
                   "2 -> Exit\n"
                   "-------------------------------\n"
                   "Choose a branch >>> "
                   )
    if branch == '1':
        pass
    elif branch == '2':
        break
    else:
        print("Invalid input!\n"
              "Process finished!"
              )
        break
    x_inputs = ''
    o_inputs = ''

    print("\n----------------------\n"
          "Game started ⚠️")
    step = 1
    victory = False
    while step < 10:
        if step % 2 == 1:
            x_input = input("------------------------------------------\n"
                            + template + "❌: (0-9) oraliqda son kiriting: ")
            while x_input not in ['1', '2', '3', '4', '5', '6', '7', '8', '9'] or x_input in x_inputs:
                x_input = input("----------------------------------------\n" +
                                template + "👎👎👎Xato urinish👎👎👎\n"
                                "❌: (0-9) oraliqda son kiriting: "
                                )
            x_inputs += x_input
            template = template.replace(x_input, "❌")

            for v in victories:
                if v[0] in x_inputs and v[1] in x_inputs and v[2] in x_inputs:
                    victory = True

        if step % 2 == 0:
            o_input = input("-------------------------------------------\n"
                            + template + "🔴: (0-9) oraliqda son kiriting: ")
            while o_input not in ['1', '2', '3', '4', '5', '6', '7', '8', '9'] or o_input in o_inputs:
                x_input = input("----------------------------------------\n" +
                                template + "👎👎👎Xato urinish👎👎👎\n"
                                "🔴: (0-9) oraliqda son kiriting: "
                                )
            o_inputs += o_input
            template = template.replace(o_input, "🔴")

            for v in victories:
                if v[0] in o_inputs and v[1] in o_inputs and v[2] in o_inputs:
                    victory = True
        if victory:
            if step % 2 == 1:
                print("-----------------------------------------------\n" +
                      template + "❌ o'yinchi g'alaba qozondi! 🎉🎉🎉\n"
                      "-----------------------------------------------\n"
                      )
            elif step % 2 == 0:
                print("-----------------------------------------------\n" +
                      template + "🔴 o'yinchi g'alaba qozondi! 🎉🎉🎉\n"
                      "-----------------------------------------------\n"
                      )
            break
        step += 1
    else:
        print("Durrang natija")
        print(template)
