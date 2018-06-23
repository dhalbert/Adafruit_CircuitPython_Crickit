# The MIT License (MIT)
#
# Copyright (c) 2018 Dan Halbert for Adafruit Industries
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""
`adafruit_crickit.terminals`
============================

Mapping of terminal names on an Adafruit Crickit board to their seesaw pin numbers.

* Author(s): Dan Halbert
"""

from micropython import const

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_Crickit.git"

SIGNAL1 = const(2)
SIGNAL2 = const(3)
SIGNAL3 = const(40)
SIGNAL4 = const(41)
SIGNAL5 = const(11)
SIGNAL6 = const(10)
SIGNAL7 = const(9)
SIGNAL8 = const(8)

_SIGNAL_SET = set((SIGNAL1, SIGNAL2, SIGNAL3, SIGNAL4, SIGNAL5, SIGNAL6, SIGNAL7, SIGNAL8))

SERVO1 = const(14)
SERVO2 = const(15)
SERVO3 = const(16)
SERVO4 = const(17)

_SERVO_SET = set((SERVO1, SERVO2, SERVO3, SERVO4))

MOTOR1A = const(22)
MOTOR1B = const(23)
MOTOR2A = const(19)
MOTOR2B = const(18)

_MOTOR1_SET = set((MOTOR1A, MOTOR1B))
_MOTOR2_SET = set((MOTOR2A, MOTOR2B))
_MOTOR_SET = _MOTOR1_SET | _MOTOR2_SET

#  Drive terminals numbers on the FeatherWing Crickit. are the reverse of those on the CPX Crickit.

CPX_DRIVE1 = const(42)
CPX_DRIVE2 = const(43)
CPX_DRIVE3 = const(12)
CPX_DRIVE4 = const(13)

FEATHER_DRIVE1 = const(13)
FEATHER_DRIVE2 = const(12)
FEATHER_DRIVE3 = const(43)
FEATHER_DRIVE4 = const(42)

_DRIVE_SET = set((CPX_DRIVE1, CPX_DRIVE2, CPX_DRIVE3, CPX_DRIVE4))

_PWM_SET = _MOTOR_SET | _SERVO_SET | _DRIVE_SET

TOUCH1 = const(4)
TOUCH2 = const(5)
TOUCH3 = const(6)
TOUCH4 = const(7)

_TOUCH_SET = set((TOUCH1, TOUCH2, TOUCH3, TOUCH4))

NEOPIXEL = 20