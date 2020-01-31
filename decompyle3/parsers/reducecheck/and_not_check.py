#  Copyright (c) 2020 Rocky Bernstein


def and_not_check(
    self, lhs: str, n: int, rule, ast, tokens: list, first: int, last: int
) -> bool:
    jmp = ast[1]
    if jmp.kind.startswith("jmp_"):
        if last == n:
            return True
        jmp_target = jmp[0].attr
        jmp_offset = jmp[0].offset

        if tokens[first].off2int() <= jmp_target < tokens[last].off2int():
            return True
        if rule == ("and_not", ("expr", "jmp_false", "expr", "POP_JUMP_IF_TRUE")):
            jmp2_target = ast[3].attr
            return jmp_target != jmp2_target
        return jmp_target != tokens[last].off2int()
    return False
