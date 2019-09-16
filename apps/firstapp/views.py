from django.shortcuts import render, request, redirect, random



# def process_gold(building):
#     """
#     returns the amount of gold proccessed this turn
#     """
#     # get a random amount of gold, depending on the building
#     if building  == "cave":
#         amount = random.randint(1,3)

#     elif building == 'grandma':
#         amount = random.randint(3,5)
#     elif building == 'dungeon':
#         amount = random.randint(2,5)
#     else:
#         # CASINO LOGIC
#         # get_money says if we won/lost
#         get_money = True

#         # casino_result tells us get_money
#         casino_result = random.randint(0,1)

#         if casino_result == 0:
#             get_money = False
        
#         amount = random.randint(20,50)

#     return amount

# def index():
#     # check if "golds" is in session
#     if not "golds" in session:
#         # set golds to 0
#         session["golds"] = 0

#     if not "messages" in session:
#         session["messages"] = ["Welome to Ninja Gold"]

#     print(session["messages"])
#     return ("firstapp/index.html")

# @app.route("/gold", methods=["POST"])
# def golding():

#     result = "got"

#     # we can have different buildings!
#     print(request.form)
#     building = request.form["building"]

#     # build a message
#     # "You just got {{ amount }} from the {{ building }}

#     result = "got"
    
#     amount = process_gold(request.form["building"])

#     if amount < 0:
#         result = "lost"
#         amount = amount * -1

#     # update sesion["golds"] by that amount
#     session["messages"].append(f"You just <span class={result}>{result}</span> {abs(amount)} from the {building}")
#     session["golds"] += amount

#     return redirect('/')

