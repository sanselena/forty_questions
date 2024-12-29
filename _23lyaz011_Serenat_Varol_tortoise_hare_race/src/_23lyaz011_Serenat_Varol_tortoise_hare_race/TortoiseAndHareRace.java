package _23lyaz011_Serenat_Varol_tortoise_hare_race;

import java.util.Random;

public class TortoiseAndHareRace {

    public static void main(String[] args) {
        Random random = new Random();
        int tortoisePosition = 1;
        int harePosition = 1;
        int finishLine = 70;

        while (tortoisePosition < finishLine && harePosition < finishLine) {
        	
            // Tortoise moves
            int tortoiseMove = random.nextInt(10) + 1;
            if (tortoiseMove <= 5) {
                tortoisePosition += 3; // Fast plod
            } else if (tortoiseMove <= 7) {
                tortoisePosition -= 6; // Slip
            } else {
                tortoisePosition += 1; // Slow plod
            }

            // Make sure tortoise doesn't go below position 1
            if (tortoisePosition < 1) {
                tortoisePosition = 1;
            }

            // Hare moves
            int hareMove = random.nextInt(10) + 1;
            if (hareMove <= 2) {
                // Sleep, no movement
            } else if (hareMove <= 4) {
                harePosition += 9; // Big hop
            } else if (hareMove == 5) {
                harePosition -= 12; // Big slip
            } else if (hareMove <= 8) {
                harePosition += 1; // Small hop
            } else {
                harePosition -= 2; // Small slip
            }

            // Make sure hare doesn't go below position 1
            if (harePosition < 1) {
                harePosition = 1;
            }

            System.out.println("Tortoise position: " + tortoisePosition + ", Hare position: " + harePosition);

            if (tortoisePosition == harePosition) {
                System.out.println("OUCH! Tortoise and Hare bumped into each other!");
            }
        }

        if (tortoisePosition >= finishLine && harePosition >= finishLine) {
            System.out.println("It's a tie!");
        } else if (tortoisePosition >= finishLine) {
            System.out.println("Tortoise wins!");
        } else {
            System.out.println("Hare wins!");
        }
    }
}
