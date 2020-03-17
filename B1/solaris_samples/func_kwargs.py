
#principle, timex, rate
def simple_int(**kwargs):
    principle = kwargs["principle"]
    timex = kwargs["timex"]
    rate = kwargs["rate"]
    si = (principle * timex * 12 * rate) / 100
    return si, principle

#{"rate":2, "timexa":3, "principle":20000}
def simple_int2(**kwargs):
    principle = kwargs.get("principle", 1)
    timex = kwargs.get("timex", 0)
    rate = kwargs.get("rate", 0)
    si = (principle * timex * 12 * rate) / 100
    return si, principle
val = simple_int2(timex=3, principle=20000, rate=2)
print(val)