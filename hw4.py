{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "ab608d8a-fead-45f9-9349-ad29292e2f9e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Input his/her name:  qwkd\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "-----------------\n",
      "Hello qwkd,\n",
      "Welcome to Seoul.\n",
      "-----------------\n"
     ]
    }
   ],
   "source": [
    "def rep_char(c,n):\n",
    "    print(f'{c}'*n)\n",
    "\n",
    "\n",
    "\n",
    "name = input('Input his/her name: ')\n",
    "\n",
    "def welcome(names):\n",
    "    msg1 = ('Hello %s,' %names)\n",
    "    msg2 = 'Welcome to Seoul.'\n",
    "\n",
    "    nstr = len(msg1) if (len(msg1) > len(msg2)) else len(msg2)\n",
    "    rep_char('-',nstr)\n",
    "    print(msg1)\n",
    "    print(msg2)\n",
    "    rep_char('-',nstr)\n",
    "    \n",
    "\n",
    "    return nstr\n",
    "n = welcome(name)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "57732e73-7024-4c40-a34f-fffeb645f9b9",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
