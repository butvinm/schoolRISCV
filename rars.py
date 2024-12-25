reg_numbers = {
    "zero": 0,
    "ra": 1,
    "sp": 2,
    "gp": 3,
    "tp": 4,
    "t0": 5,
    "t1": 6,
    "t2": 7,
    "s0": 8,
    "s1": 9,
    "a0": 10,
    "a1": 11,
    "a2": 12,
    "a3": 13,
    "a4": 14,
    "a5": 15,
    "a6": 16,
    "a7": 17,
    "s2": 18,
    "s3": 19,
    "s4": 20,
    "s5": 21,
    "s6": 22,
    "s7": 23,
    "s8": 24,
    "s9": 25,
    "s10": 26,
    "s11": 27,
    "t3": 28,
    "t4": 29,
    "t5": 30,
    "t6": 31,
}


cmd = ""
while cmd != "exit":
    try:
        cmd = input()
    except EOFError:
        break

    parts = cmd.split()

    match parts:
        case "pop", src_name:
            src = bin(reg_numbers[src_name])[2:].zfill(5)
            cmd_bin = '00000000' + '00000' + src + '000' + src + '0011011'
            cmd_hex = hex(int(cmd_bin, base=2))[2:].zfill(8)
            print(cmd_hex)
        case "push", src_name:
            src = bin(reg_numbers[src_name])[2:].zfill(5)
            cmd_bin = '00000000' + '00000' + src + '001' + '00000' + '0011011'
            cmd_hex = hex(int(cmd_bin, base=2))[2:].zfill(8)
            print(cmd_hex)
        case "set", dst_name, value:
            dst = bin(reg_numbers[dst_name])[2:].zfill(5)
            value_bin = bin(int(value))[2:].zfill(12)

            cmd_hex = "00000533"
            print(cmd_hex)

            cmd_bin = value_bin + dst + '000' + dst + '0010011'
            cmd_hex = hex(int(cmd_bin, base=2))[2:].zfill(8)
            print(cmd_hex)
