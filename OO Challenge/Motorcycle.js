class Motorcycle extends Vehicle{
    
    constructor(make, model, year){
        super(make, model, year);
        this.numWheels = 2; 
    }
    revEngine(){
        return 'VROOM!!!';
    }
}