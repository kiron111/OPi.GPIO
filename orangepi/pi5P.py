# -*- coding: utf-8 -*-
# Copyright (c) 2018 Richard Hull & Contributors
# See LICENSE.md for details.

"""

Usage:

.. code:: python
   import orangepi.5P
   from OPi import GPIO

   GPIO.setmode(orangepi.5P.BOARD) or GPIO.setmode(orangepi.5P.BCM)
"""

# pin number = (position of letter in alphabet - 1) * 32 + pin number
# So, PD14 will be (4 - 1) * 32 + 14 = 110

# Orange Pi 5P physical board pin to GPIO pin
BOARD = {
   3:16,    # GPIO0_C0/I2C2_SDA_M0/PWM1_M0 (fd8b0010)/CAN0_RX_M0
   5:15,    # GPIO0_B7/I2C2_SCLM0/PWM0_M0 (fd8bOOOO)/CAN0_TX_M0
   7:62,    # GPIO1_06/PWM14_M2 (febf0020)/I2C8_SCL_M2/UART1_RTSN_M1
   8:109,    # GPIO1_A1/UART6_TX_M1/I2C2_SCLM4/SPI4_MOSI_M2
   10:110,    # GPIOLA0/UART6_RX_M1/I2C2_SOA_M4/SPI4_MISO_M2
   11:36,    # GPIO1_A4
   12:97,    # GPIO3_A1SPI4_MOSI_M1/PWM11_IR_M0 (febe0030)
   13:39,    # GPIO1_A7
   15:40,    # GPIO1_B0
   16:32,    # GPIO3_B5/UART3_TX_M1/CAN1_RX_M0/PWM12_M0 (febfOOOO)
   18:33,    # GPIO3_86/UART3_RX_M1/CAN1_TX_M0/PWM13_M0 (febf0010l)
   19:42,    # GPIO1_B2/SPIO_MOSI_M2/UART4_RX_M2
   21:41,    # GPIO1_B1/SPIO_MISO_M2
   22:34,    # GPIO1_A2/UART6_RTSN_M1/I2C4_SOA_M3/SPI4_CLK_M2/PWM0_M2 (fd8b0000)
   23:43,    # GPIO1_B3/SPIO_CLK_M2/UART4_TX_M2
   24:44,    # GPIO1_84/SPIO_CS0_M2/UART7_RX_M2
   26:45,    # GPIOl_B5/SPIO_CS1_M2/UART7_TX_M2
   27:47,    # GPIO1_B7/I2C5_SDA_M3/UART1_RX_M1/PWM13_M2 (febf0010)
   28:46,    # GPIO1_B6/I2C5_SCL_M3/UART1_TX_M1
   29:63,    # GPIO1_D7/I2C8_SOA_M2/UARTl_CTSN_M1
   31:96,    # GPIO3_A0SPI4_MISO_M1/PWM10_M0 (febe0020)
   32:35,    # GPIO1_A3/UART6_CTSN_M1/I2C4_SCL_M3PWM1_M2 (fd8b0010)
   33:114,    # GPIO3_C2/PWM14_M0 (febf0020)
   35:98,    # GPIO3_A2/UART8_TX_M1/SPI4_CLK_M1
   36:101,    # GPIO3_A5/UART8_CTSN_M1
   37:113,    # GPIO3_C1
   38:100,    # GPIO3_A4/UART8_RTSN_M1/SPI4_CS1_M1
   40:99,    # GPIO3_A3/UART8_RX_M1/SPI4_CS0_M1
   }

# No reason for BCM mapping, keeping it for compatibility
BCM = BOARD
