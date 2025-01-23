def gears(rack: list, n: int, m: int):
    gear_dict_n = {}
    gear_dict_m = {}
    
    for box in rack:
        for gear in box:
            if gear > 0:
                if gear % n == 0:
                    ratio_n = gear // n
                    if ratio_n in gear_dict_m:
                        return (gear, gear_dict_m[ratio_n])
                    gear_dict_n[ratio_n] = gear
                
                if gear % m == 0:
                    ratio_m = gear // m
                    if ratio_m in gear_dict_n:
                        return (gear_dict_n[ratio_m], gear)
                    gear_dict_m[ratio_m] = gear

    return (None, None)