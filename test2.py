class Stack:
    def __init__(self):
        self.stack=[]

    def stpush(self,data):
        self.stack.insert(data)
        print(self.stack)

    def stpop(self):
        if len(self.stack) <= 0:
            print("STack empty")
        else:
            k = self.stack.pop()
            print("Popped elemen is", k)

    def stpeek(self):
        if len(self.stack) <= 0:
            print("STack empty")
        else:
            print("Element on front is ", self.stack[-1])

    def stprint(self):
        if len(self.stack) <= 0:
            print("STack empty")
        else:
            print(self.stack)

st = Stack()
st.stpush(1)
st.stpush(2)
st.stpeek()
st.stpush(3)
st.stpush(4)

st.stprint()
st.stpeek()
st.stpop()
st.stpeek()
st.stpop()
st.stprint()
st.stpop()
st.stpop()
st.stpop()
st.stpop()
st.stpop()


