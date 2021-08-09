public class CuerpoDeAgua {

    // Fields (Attributes)
    private String name;
    private int id;
    private String municipality;
    private double irca;

    // Constructors
    public CuerpoDeAgua(String name, int id, String municipality, double irca) {
        this.name = name;
        this.id = id;
        this.municipality = municipality;
        this.irca = irca;
    }

    // Methods
    // Getter methods
    public String getName() {
        return name;
    }

    public double getId() {
        return id;
    }

    public String getMunicipality() {
        return municipality;
    }

    public double getIrca() {
        return irca;
    }

    // Nivel method
    public String nivel() {

        String riskLevel = "";

        if (irca >= 80.1 && irca <= 100) {
            riskLevel = "INVIABLE SANITARIAMENTE";
        } else if (irca >= 35.1 && irca <= 80) {
            riskLevel = "ALTO";
        } else if (irca >= 14.1 && irca <= 35) {
            riskLevel = "MEDIO";
        } else if (irca >= 5.1 && irca <= 14) {
            riskLevel = "BAJO";
        } else if (irca >= 0 && irca <= 5) {
            riskLevel = "SIN RIESGO";
        } else {
            riskLevel = "VALOR NO VALIDO";
        }

        return riskLevel;
    }

}