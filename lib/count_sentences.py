#!/usr/bin/env python3

class MyString:
  pass
  def __init__(self,value="nm"):
    self.value=value

  @property
  def value(self):
    return self._value
  
  @value.setter
  def value(self,value):
    if(type(value)==str):
      self._value=value
    else:
      print("The value must be a string.")
  
  def is_sentence(self):
    return self.value.endswith(".")

  def is_question(self):
    return self.value.endswith("?")

  def is_exclamation(self):
    return self.value.endswith("!")
  
  def count_sentences(self):
    pass
    w=self.value.replace("?",".")
    z=w.replace("!",".")
    print(z.split(". "))
    if(". " in z):
      return len(z.split(". "))
    else:
      return 0

