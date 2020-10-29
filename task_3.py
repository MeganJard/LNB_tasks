def is_correct(*args):
    answer = 0.
    errs_conter = 0
    for i in args:
        data = open(i).readlines()
        for j in data:
            try:
                answer += sum([1 / float(k) for k in j.split()])
            except Exception:
                errs_conter += 1
                break
    return answer, errs_conter

