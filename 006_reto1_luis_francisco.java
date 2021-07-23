import java.util.Scanner;

public class reto1 {
    public static void main(String[] args) {

        // Read data from the user
        Scanner scanner = new Scanner(System.in);
        // The number of water bodies is require but
        // your really don't need it in the program
        int numberWaterBodies = scanner.nextInt();
        // Remember:
        // https://stackoverflow.com/questions/48702108/print-entire-line-string-with-java-scanner
        scanner.nextLine();
        String[] ircaString = scanner.nextLine().split(" ");
        scanner.close();

        // Convert the string into an array which contain doubles
        double[] ircaDouble = numbersStringToDouble(ircaString);

        // Identify the mean risk level of the data
        String meanRiskLevel = identifyRiskLevel(meanArrayDouble(ircaDouble));

        // Identify the percentage of water bodies with risk levels BAJO
        // and Medio
        double percentageBajoMedio = ((double) (countRiskLevelCategory(ircaDouble, "BAJO")
                + countRiskLevelCategory(ircaDouble, "MEDIO")) / ircaDouble.length) * 100;
        String percentageBajoMedioFormatted = String.format("%.2f", percentageBajoMedio);

        // Identify if there are more than one water body with a risk level INVIABLE
        // SANITARIAMENTE
        String isMoreThanOne = "NO";
        if (countRiskLevelCategory(ircaDouble, "INVIABLE SANITARIAMENTE") > 1) {
            isMoreThanOne = "SI";
        }

        // Print results
        System.out.println(meanRiskLevel);
        System.out.println(percentageBajoMedioFormatted);
        System.out.println(isMoreThanOne);

    }

    // Convert an array of string numbers to double
    public static double[] numbersStringToDouble(String[] numbersString) {

        double[] numbersDouble = new double[numbersString.length];

        for (int i = 0; i < numbersString.length; i++) {
            numbersDouble[i] = Double.parseDouble(numbersString[i]);
        }

        return numbersDouble;

    }

    // Identify the risk level
    public static String identifyRiskLevel(double level) {

        String riskLevel = "";

        if (level >= 80.1 && level <= 100) {
            riskLevel = "INVIABLE SANITARIAMENTE";
        } else if (level >= 35.1 && level <= 80) {
            riskLevel = "ALTO";
        } else if (level >= 14.1 && level <= 35) {
            riskLevel = "MEDIO";
        } else if (level >= 5.1 && level <= 14) {
            riskLevel = "BAJO";
        } else if (level >= 0 && level <= 5) {
            riskLevel = "SIN RIESGO";
        } else {
            riskLevel = "VALOR NO VALIDO";
        }

        return riskLevel;

    }

    // Count the number of instances of a risk level category
    public static int countRiskLevelCategory(double[] array, String category) {

        String[] arrayRiskLevel = new String[array.length];
        int countCategory = 0;

        for (int i = 0; i < array.length; i++) {
            arrayRiskLevel[i] = identifyRiskLevel(array[i]);

            if (arrayRiskLevel[i].equals(category)) {
                countCategory++;
            }
        }

        return countCategory;

    }

    // Calculate the mean
    public static double meanArrayDouble(double[] ArrayDouble) {

        double sum = 0;
        for (int i = 0; i < ArrayDouble.length; i++) {
            sum += ArrayDouble[i];
        }

        double mean = sum / ArrayDouble.length;
        return mean;

    }

}
