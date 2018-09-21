
def get_list (holders):
    
    result = []
    total_percent = 0

    for rank, holder in enumerate(holders):
        print(holder)

        percent = float(holder[3].replace("%", ""))
        total_percent += percent
        address = holder[1].replace("0x", "")
        amount = holder[2]

        result.append (
            {
                'rank'    : (rank+1),
                'amount'  : amount,
                'address' : address, 
                'percent' : percent,
                'total_percent' : total_percent
            }
        )

    return result