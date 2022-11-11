"""Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the software.

Patients' data is held in an inflammation table (2D array) where each row contains 
inflammation data for a single patient taken over a number of days 
and each column represents a single day across all patients.
"""

import numpy as np


def load_csv(filename):
    """Load a Numpy array from a CSV

    :param filename: Filename of CSV to load
    """
    return np.loadtxt(fname=filename, delimiter=',')


def daily_mean(data):
    """Calculate the daily mean of a 2D inflammation data array.
    :param data: A 2D array containing the inflammation data for all patients.
    :returns: A 1D array of the mean value of inflammation for each day.
    """
    return np.mean(data, axis=0)


def daily_max(data):
    """Calculate the daily max of a 2D inflammation data array.
    :param data: A 2D array containing the inflammation data for all patients.
    :returns: A 1D array of the maximum value of inflammation for each day.
    """
    return np.max(data, axis=0)


def daily_min(data):
    """Calculate the daily min of a 2D inflammation data array.
    :param data: A 2D array containing the inflammation data for all patients.
    :returns: A 1D array of the minimum value of inflammation for each day.
    """
    return np.min(data, axis=0)

def patient_normalise(data):
    """Normalise patient data from a 2D inflammation data array."""

    if type(data) is not np.ndarray:
        raise TypeError("Input must be a 2D numpy array")
        
    if np.any(data < 0):
        raise ValueError("Inflammation values cannot be negative.")
    
    if len(data.shape) != 2:
        raise ValueError("Data array must be 2D")

    maxima = np.nanmax(data, axis=1)
    with np.errstate(invalid='ignore', divide='ignore'):
        normalised = data / maxima[:, np.newaxis]
    normalised[np.isnan(normalised)] = 0
    normalised[normalised < 0] = 0
    return normalised

data = np.array([1., 2., 3.])
names = ['Jane', 'Yaz', 'Dan']


def attach_names(data, names):
    output = []
    assert len(data) == len(names)
    for data_row, name in zip(data, names):
        output.append({
            'name': name,
            'data': data_row
            })
    return output
    
attached_names = attach_names(data, names)
print(attached_names)



class Observation:
    def __init__(self, day, value):
        self.day = day
        self.value = value

    def __str__(self):
        return self.value


class Person:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name

class Doctor(Person):
    def __init__(self, name):
        super().__init__(name)
        self.list_patients = []
    
    def add_patient(self, patient_name):
        for patient in self.list_patients:
            if patient_name == patient:
                return
        self.list_patients.append(patient_name)

class Patient(Person):
    def __init__(self, name, observations=None):
        super().__init__(name)
        self.observations = []
        if observations is not None:
            self.observations = observations

    def __str__(self):
        return self.name
    
    @property
    def last_observation(self):
        return self.observations[-1]

    def add_observation(self, observed_value, day=None):
        if day is None:
            try:
                day = self.observations[-1].day + 1
            except IndexError:
                day = 0

        new_observation = Observation(day, observed_value)
        self.observations.append(new_observation)

# alice = Patient('Alice')
# print(alice)
# alice.add_observation(3)
# alice.add_observation(4)
# alice.add_observation(5, 3)
# print(alice.observations)
# print(alice.last_observation)



# class Book:
#     def __init__(self, book_name, author):
#         self.title = book_name
#         self.author = author
    
#     def __str__(self):
#         return (f"{self.title} by {', '.join(self.author)}")

# uni_physics = Book('University Physics with Modern Physics', 'H. Young')

# print(uni_physics)

# class Library:
#     def __init__(self):
#         self.books = []

#     def __len__(self):
#         return len(self.books)

#     def __getitem__(self, key):
#         return self.books[key]

#     def add_book(self, title, author):
#         self.books.append(Book(title, author))
    
#     def by_author(self, author):
#         matches = []
#         for book in self.books:
#             if book.author == author:
#                 matches.append(book)

#         if not matches:
#             raise KeyError('Author does not exist')

#         return matches

# lib = Library()
# lib.add_book(uni_physics)
# lib.by_author("H. Young")

# from functools import reduce

# sequence = ['-1', '-4', '3']

# def sum_of_squares(sequence):
#     sequence = [float(str) for str in sequence if str[0] != '#']
#     square = [num**2 for num in sequence]
#     return reduce(lambda a, b: a + b, square)


# print('Sum of squares is:', sum_of_squares(sequence))



