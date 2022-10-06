balloons = int(input("Enter the number of balloons: "))
children = int(input("Enter the number of children: "))
balloons1 = balloons // children
balloonsR = balloons % children
print(f"""
Balloons per child: {balloons1}
Balloons left over: {balloonsR}
""")