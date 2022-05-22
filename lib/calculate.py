# dictionary to stor the charachter referening to each cardinal compass direction (E, N, W, S) with the value of the
# angle associated to it. Assuming the East refers to zero and moving anticlock wise means the angle increases,
# to reach 90 at the north and so on. Will be used later.
from pprint import pprint

directions = {'E': 0, 'N': 90, 'W': 180, 'S': 270}
# dictionary stor the the angle values as a string, will be used later
directions_inv = {'0': 'E', '90': 'N', '180': 'W', '270': 'S'}


class MarsRover():
    # a list will be used to check the input
    direction_letters = ['E', 'N', 'W', 'S']

    """intial function for the MarsRover class"""

    def __init__(self, instructions: list, current_position: list, upper_right_corner: list):

        self.current_position = current_position  # referes to the current position of the rover  (e.g., 1 2 N)
        self.instructions = instructions  # the instructions given by the user (e.g., LMRMMM)
        self.upper_right_corner = upper_right_corner  # the values of the upper right corner

    """performs the right rotation"""

    def r_rotation(self):
        angle = directions[self.current_position[
            2]] - 90  # takes the angle associated with each compass direction and subtract 90 from it
        angle = angle % 360  # takes care of the boundary condition
        self.current_position[2] = directions_inv[
            str(angle)]  # after subtracting giving the result angle, this gives the direction associated with it
        return self.current_position[0], self.current_position[1], self.current_position[2]

    """performs the left rotation"""

    def l_rotation(self):
        angle = directions[self.current_position[
            2]] + 90  # takes the angle associated with each compass direction and add 90 from it
        angle = angle % 360  # takes care of the boundary condition
        self.current_position[2] = directions_inv[
            str(angle)]  # after subtracting giving the result angle, this gives the direction associated with it
        return self.current_position[0], self.current_position[1], self.current_position[2]

    """For heading forward with no change in the direction"""

    def moving_forward(self):
        pos = self.current_position[:]  # defines a list of the input of the rovers current position
        pos[0] = self.current_position[0]  # the x value of the current position
        pos[1] = self.current_position[1]  # the y value of the y position

        if directions[self.current_position[
            2]] == 90:  # if the current direction is N and the angle is 90, the with this function, 1 should be added to the y value
            pos[1] = int(pos[1]) + 1
        elif directions[self.current_position[
            2]] == 270:  # if the current direction is S and the angle is 90, the with this function, 1 should be subtracted to the y value
            pos[1] = int(pos[1]) - 1
        elif directions[self.current_position[
            2]] == 180:  # if the current direction is W and the angle is 90, the with this function, 1 should be subtracted to the x value
            pos[0] = int(pos[0]) - 1
        elif directions[self.current_position[
            2]] == 0:  # if the current direction is E and the angle is 90, the with this function, 1 should be added to the x value
            pos[0] = int(pos[0]) + 1
        return pos

    """"performs the different moves: either in the direction or moving forward with no change in the direction"""

    def general_movement(self):

        for command in self.instructions:
            if command == 'L':  # if the given command in the instructions of the user is 'L', then the l-rotation function will be run
                self.current_position[0], self.current_position[1], self.current_position[2] = self.l_rotation()
            elif command == 'R':  # if the given command in the instructions of the user is 'R', then the r-rotation function will be run
                self.current_position[0], self.current_position[1], self.current_position[2] = self.r_rotation()
            elif command == 'M':  # if the given command in the instructions of the user is 'M', then the Moving_forward function will be run
                self.current_position[0], self.current_position[1], self.current_position[2] = self.moving_forward()

        """To check that the output values of x and y are not negative values."""
        x_pos = self.current_position[0]  # defines the x value of the rover's last position
        y_pos = self.current_position[1]  # defines the y value of the rover's last position
        dirn = self.current_position[2]  # defines the cardinal compass direction of the rover's last position

        if (int(x_pos) < 0 or int(y_pos) < 0):
            raise Exception(
                "The last position of the rover, should have only positive x and y values. Sorry, start again!")

        return self.current_position

    """Checking that the input values are in the required formate and does not exceed the upper right corner limit"""

    def checking_the_input(self):
        x_upp_right = self.upper_right_corner[0]  # defines the X value of the upper right corner
        y_upp_right = self.upper_right_corner[1]  # defines the X value of the upper right corner

        if (
                len(self.current_position) != 3):  # Makes sure that the input of the current position is 3 values separated by a space
            raise Exception(
                "The current Position of the rover should be 3 values (as :X_value Y_value cardinal compass direction), separated by a space. Try again!")

        x_pos = self.current_position[0]  # defines the x value of the rover's current position
        y_pos = self.current_position[1]  # defines the y value of the rover's current position
        dirn = self.current_position[2]  # defines the cardinal compass direction of the rover's current position

        if (
                not x_pos.isdigit() or not y_pos.isdigit()):  # Makes sure that the current X_value and Y_value are integers
            raise Exception("X and Y values should be positive numbers only. Try again!. ")

        if (int(x_pos) > int(x_upp_right) or int(y_pos) > int(
                y_upp_right)):  # Makes sure that the x and y values are not more than the x and y values of the upper right corner.
            raise Exception("X and y values should be less than the upper right corner values. Try again!")

        if (
                not dirn.isalpha() or dirn not in MarsRover.direction_letters):  # Makes sure that the given direction is only E (for East) or W (for West) or S (for South) or N (for North)
            raise Exception(
                "The given direction should be on of the cardinal compass direction (as a one letter: E or W oe S or N). Try again!")

        if (self.instructions.isalpha() == False or all(chars in ['L', 'R', 'M'] for chars in
                                                        self.instructions) == False):  # Makes sure that the given instructions are on of the following: R or M or L
            raise Exception("Instructions should be in a form of letters and only L or R or M. Try again!")


def calc(instructions, current_position, upper_right_corner):
    rover2 = MarsRover(
        instructions,
        current_position,
        upper_right_corner)
    rover2.checking_the_input()
    return rover2.general_movement()

def main():
    while True:
        try:
            upp_right_corner = input("Enter x-value and y-value of the upper right corner of the Plateau: \n").split()

            x_upp_right = int(upp_right_corner[0])  # giving the x-value of the upper right corner as an integer
            y_upp_right = int(upp_right_corner[1])  # giving the y-value of the upper right corner as an integer
            assert x_upp_right > 0  # makes sure the x-value of the upper right corner is only a positive value, otherwise an assertion error will be given
            assert y_upp_right > 0  # makes sure the x-value of the upper right corner is only a positive value, otherwise an assertion error will be given
            break
        except AssertionError:
            print(
                "Only positive integer co ordinates accepted for the upper right corner of the Plateau. Please try again!")

    while True:
        try:
            rover1 = MarsRover(current_position=input("Enter the current position of the rover 1: \n").split(),
                               instructions=input("Enter the instructions of the rover: \n"),
                               upper_right_corner=upp_right_corner)  ## Object of class Rovers
            rover1.checking_the_input()
            print("The output is: ", rover1.general_movement())
            break
        except Exception as ex:
            print(ex)
            # Note about the upper right corner: I was not sure if the upper right corner should be given as an input with every time you give instructions to a rover.
    # Or it should be givin only one time at the start of the mission. However, I chose here to make it given everytime the instructions are given, just to be in the safe side.

    while True:
        try:
            rover2 = MarsRover(current_position=input("Enter the current position of the rover 2: \n").split(),
                               instructions=input("Enter the instructions of the rover: \n"),
                               upper_right_corner=upp_right_corner)  ## Object of class Rovers
            rover2.checking_the_input()
            print("The final position of rover 2 is: ", rover2.general_movement())
            break
        except Exception as ex:
            print(ex)

    # Note about the number of rovers: I was thinking to creat a function to ask the user/scientist to add the rover's ID,
    # as they are more than one. However, there was no mention in the input example in the problem of the rover's ID. So
    # I chose just two rovers as the input given are for only two rovers.


if __name__ == "__main__":
    main()
