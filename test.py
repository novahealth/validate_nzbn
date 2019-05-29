import validate_nzbn

t = validate_nzbn.validate_nzbn("999sadfs99asd91222ss2399asdfasdf99")

x = validate_nzbn.validate_nzbn("92ksj38474skdm3829aa10")

y = validate_nzbn.validate_nzbn("699sadfs99asd91222ss2399asdfasdf99")

print(t, "should be false")
print(x, "should be true")
print(y, "should be false")

# if t:
#     print(t)
# else:
#     print("False")
