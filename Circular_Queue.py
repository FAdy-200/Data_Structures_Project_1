class CircularDeque:
    def __init__(self, capacity: int):
        """
        Initialize your data structure here.
        Set the maximum size of the deque to be capacity.
        """
        self.capacity = capacity
        self.deque = [0] * capacity
        self.front = self.rear = -1

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque.
        Return true if the operation is successful.
        """
        if self.isEmpty()==True:    # empty queue
            self.front=0
            self.rear=0
            self.deque[self.front]=value
            return True
        elif self.isFull()==True:   # full queue

            return "False, Queue is Full"

        else:
            if self.front-1==-1:    # if the current front is the first element
                self.front = self.capacity - 1
                self.deque[self.front] = value
                return True

            else:                   # normal insertion
                self.front -= 1
                self.deque[self.front] = value
                return True



    def insertRear(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque.
        Return true if the operation is successful.
        """
        if self.isEmpty() == True:
            self.front = 0
            self.rear=0
            self.deque[self.front] = value
            return True
        elif self.isFull()==True:

            return "False, Queue is Full"
        else:
            try:            # normal insertion
                self.rear+=1
                self.deque[self.rear]=value
                return True
            except:         # if there is an error this means that it reached the end and circulating
                self.rear=0
                self.deque[self.rear] = value
                return True


    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque.
        Return true if the operation is successful.
        """
        if self.isEmpty()==True:                # if there is no elements then no deletion will happen
            return False
        else:
            if self.front==self.rear:           # in case there is only one element in the queue
                self.front=-1
                self.rear=-1
            elif self.front+1 <self.capacity:   # normal case
                self.front+=1
            elif self.front+1 == self.capacity: # the case if the front is at the end of the queue
                self.front=0

            return True

    def deleteRear(self) -> bool:
        """
        Deletes an item from the rear of Deque.
        Return true if the operation is successful.
        """

        if self.isEmpty() == True:  # if there is no elements then no deletion will happen
            return False
        else:
            if self.front == self.rear:  # in case there is only one element in the queue
                self.front = -1
                self.rear = -1
            elif self.rear - 1 >= 0:  # normal case
                self.rear -= 1
            elif self.rear - 1 == -1:  # the case if the front is at the end of the queue
                self.rear = self.capacity - 1
            return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        return self.deque[self.front]

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        return self.deque[self.rear]
    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return True if self.front == -1 else False

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        if (
            self.front == 0 and self.rear == self.capacity - 1
        ) or self.rear + 1 == self.front:
            return True
        return False



# capacity, value = 10, 1
# cq = CircularDeque(capacity)
# param_1 = cq.insertFront(value)
# param_2 = cq.insertRear(value)
# param_3 = cq.deleteFront()
# param_4 = cq.deleteRear()
# param_5 = cq.getFront()
# param_6 = cq.getRear()
# param_7 = cq.isEmpty()
# param_8 = cq.isFull()



myCircularDeque = CircularDeque(3)      # set the size to be 3
print(myCircularDeque.insertRear(1))    # return true
print(myCircularDeque.insertRear(2))    # return true
print(myCircularDeque.insertFront(3))   # return true
print(myCircularDeque.insertFront(4))   # return false, the queue is full
print(myCircularDeque.getRear())        # return 2
print(myCircularDeque.isFull())         # return true
print(myCircularDeque.deleteRear())     # return true
print(myCircularDeque.insertFront(4))   # return true
print(myCircularDeque.getFront())       # return 4

