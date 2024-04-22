if select_opt == StaticVariables.results[-1] and StaticVariables.is_not_rep[StaticVariables.q_No - 1]:
        StaticVariables.marks += 1
        StaticVariables.is_not_rep[StaticVariables.q_No - 1] = False
        StaticVariables.is_correct[StaticVariables.q_No - 1] = True
    elif StaticVariables.is_not_rep[StaticVariables.q_No - 1] and select_opt == StaticVariables.results[-1] and not StaticVariables.is_correct[StaticVariables.q_No - 1]:
        StaticVariables.marks += 1
        StaticVariables.is_correct[StaticVariables.q_No - 1] = True
        StaticVariables.is_not_rep[StaticVariables.q_No - 1] = False
    elif (StaticVariables.is_not_rep[StaticVariables.q_No - 1] and select_opt != StaticVariables.results[-1] and StaticVariables.is_correct[StaticVariables.q_No - 1]) or \
         (not StaticVariables.is_not_rep[StaticVariables.q_No - 1] and select_opt == StaticVariables.results[-1] and StaticVariables.is_correct[StaticVariables.q_No - 1]) or \
         (not StaticVariables.is_not_rep[StaticVariables.q_No - 1] and select_opt == StaticVariables.results[-1] and StaticVariables.is_correct[StaticVariables.q_No - 1]) or \
         (StaticVariables.is_not_rep[StaticVariables.q_No - 1] and select_opt != StaticVariables.results[-1] and not StaticVariables.is_correct[StaticVariables.q_No - 1]):
        pass
    elif not StaticVariables.is_not_rep[StaticVariables.q_No - 1] and select_opt == StaticVariables.results[-1] and not StaticVariables.is_correct[StaticVariables.q_No - 1]:
        StaticVariables.marks += 1
        StaticVariables.is_correct[StaticVariables.q_No - 1] = True
        StaticVariables.is_not_rep[StaticVariables.q_No - 1] = False
    elif not StaticVariables.is_not_rep[StaticVariables.q_No - 1] and select_opt != StaticVariables.results[-1] and StaticVariables.is_correct[StaticVariables.q_No - 1]:
        StaticVariables.marks -= 1
        StaticVariables.is_correct[StaticVariables.q_No - 1] = False
        StaticVariables.is_not_rep[StaticVariables.q_No - 1] = False
    conn.commit()
    print("next", (StaticVariables.results[-1] == select_opt))
    StaticVariables.results.clear()
    StaticVariables.q_No += 1