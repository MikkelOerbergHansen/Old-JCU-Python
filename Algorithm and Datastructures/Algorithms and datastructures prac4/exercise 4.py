

class Queue:

  # Constructor creates a list
  def __init__(self):
      self.queue = list()

  # Adding elements to queue
  def enqueue(self,data):
      # Checking to avoid duplicate entry (not mandatory)
      if data not in self.queue:
          self.queue.insert(0,data)
          return True
      return False

  # Removing the last element from the queue
  def dequeue(self):
      if len(self.queue)>0:
          return self.queue.pop()
      return ("Queue Empty!")

  # Getting the size of the queue
  def size(self):
      return len(self.queue)

  # printing the elements of the queue
  def printQueue(self):
      return self.queue


myQueue = Queue()
print(myQueue.enqueue(5))       # prints True
print(myQueue.enqueue(3))       # prints True
print(myQueue.dequeue())        # prints 5
print(myQueue.enqueue(2))       # prints True
print(myQueue.enqueue(8))       # prints True
print(myQueue.dequeue())        # prints 3
print(myQueue.dequeue())        # prints 2
print(myQueue.enqueue(9))       # prints True
print(myQueue.enqueue(1))       # prints True
print(myQueue.dequeue())        # prints 8
print(myQueue.enqueue(7))       # prints True
print(myQueue.enqueue(6))       # prints True
print(myQueue.dequeue())        # prints 9
print(myQueue.dequeue())        # prints 1
print(myQueue.enqueue(4))       # prints True
print(myQueue.dequeue())        # prints 7
print(myQueue.dequeue())        # prints 6

print(myQueue.printQueue())     # prints 4
