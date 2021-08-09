import java.util.Scanner;

public class reto2 {

    public static void main(String[] args) {

        // Read data from the user
        Scanner scanner = new Scanner(System.in);
        int numberWaterBodies = scanner.nextInt();
        // Remember:
        // https://stackoverflow.com/questions/48702108/print-entire-line-string-with-java-scanner
        scanner.nextLine();

        // Generate an array to save objects than belong
        // to the class CuerpoDeAgua
        CuerpoDeAgua[] cuerpoDeAguaArray = new CuerpoDeAgua[numberWaterBodies];

        for (int i = 0; i < numberWaterBodies; i++) {
            // Read data from the user
            String[] waterBody = scanner.nextLine().split(" ");

            // Extract data an parse if necessary to obtain
            // the correct type
            String name = waterBody[0];
            int id = Integer.parseInt(waterBody[1]);
            String municipality = waterBody[2];
            double irca = Double.parseDouble(waterBody[3]);

            // Construct each object than belongs to the class
            // CuerpoDeAgua
            CuerpoDeAgua cuerpoDeAgua = new CuerpoDeAgua(name, id, municipality, irca);
            cuerpoDeAguaArray[i] = cuerpoDeAgua;
        }

        // Close scanner
        scanner.close();

        // Print results
        printCuerpoDeAguaNameIrca(cuerpoDeAguaArray);
        printCuerpoDeAguaIrcaGreaterEqualToN(cuerpoDeAguaArray, 50);
        printCuerpoDeAguaNameRiskLevelCategory(cuerpoDeAguaArray, "ALTO");
        printCuerpoDeAguaIrcaMax(cuerpoDeAguaArray);

    }

    // Print the name and irca of each element in an array
    // with objects that belong to the class CuerpoDeAgua
    public static void printCuerpoDeAguaNameIrca(CuerpoDeAgua[] cuerpoDeAguaArray) {

        for (int i = 0; i < cuerpoDeAguaArray.length; i++) {
            System.out.println(
                    cuerpoDeAguaArray[i].getName() + " " + String.format("%.2f", cuerpoDeAguaArray[i].getIrca()));
        }

    }

    // Print the number of elements in an array with objects
    // that belong to the class CuerpoDeAgua and have an irca
    // greater or equal to some lower limit
    public static void printCuerpoDeAguaIrcaGreaterEqualToN(CuerpoDeAgua[] cuerpoDeAguaArray, double loweLimit) {

        int counter = 0;
        for (int i = 0; i < cuerpoDeAguaArray.length; i++) {
            if (cuerpoDeAguaArray[i].getIrca() >= loweLimit) {
                counter++;
            }
        }

        System.out.println(String.format("%.2f", (double) counter));

    }

    // Print the name of each element in an array with objects
    // that belong to the class CuerpoDeAgua with a specific
    // risk level
    // If there aren't elements with this specific level
    // return NA
    public static void printCuerpoDeAguaNameRiskLevelCategory(CuerpoDeAgua[] cuerpoDeAguaArray, String riskLevel) {

        int count = 0;
        for (int i = 0; i < cuerpoDeAguaArray.length; i++) {
            if (cuerpoDeAguaArray[i].nivel().equals(riskLevel)) {
                count++;
            }
        }

        if (count != 0) {
            for (int i = 0; i < cuerpoDeAguaArray.length; i++) {
                if (cuerpoDeAguaArray[i].nivel().equals(riskLevel)) {
                    System.out.print(cuerpoDeAguaArray[i].getName() + " ");
                }
            }
        } else {
            System.out.print("NA");
        }

        // We need here a new line character, \n, after the result
        System.out.println();

    }

    // Print the maximum irca in an array
    // with objects that belong to the class CuerpoDeAgua
    public static void printCuerpoDeAguaIrcaMax(CuerpoDeAgua[] cuerpoDeAguaArray) {

        double max = cuerpoDeAguaArray[0].getIrca();
        for (int i = 1; i < cuerpoDeAguaArray.length; i++) {
            if (max < cuerpoDeAguaArray[i].getIrca()) {
                max = cuerpoDeAguaArray[i].getIrca();
            }
        }

        System.out.println(String.format("%.2f", max));

    }

}
