//----------------------
//BRANCHEMENT |
//LED : sur Digital de 2 a 6 (5 pour le moment)
//PIEZO : sur Analog A0 et A1 (seulement 2 pour le moment)
//----------------------
int nombreLED = 6;
int message = 0;
short TabANA1[10];
short TabANA2[10];
short TabANA3[10];
short TabANA4[10];
short i,j,y;
bool FDeb;
short MoyANA1,MoyANA2;

void setup() {  
  Serial.begin(9600);
  MoyANA1 = 0;
  //Boucle d'initialisation des modes et mise à 0V
  for (short i = 2 ; i <= 7 ; i++) {
    pinMode(i, OUTPUT);
    digitalWrite (i, LOW);
    FDeb = false;  
  }
}

void loop() {
  //détection des impacts
  CapteurAnalog1();
  CapteurAnalog2();
  //Serial.println("Analog 0 = " + String(analogRead(0)));
  //Piezo sur A0
  /*if(analogRead(0) < MoyANA1-2)
  { 
    Serial.println(analogRead(0));
    Serial.println("Moyenne ANA1: "+String(MoyANA1));
  }
  //Piezo sur A1
  if(analogRead(1) < MoyANA2-2)
  { 
    Serial.println(analogRead(1));
    Serial.println("Moyenne ANA2: "+String(MoyANA2));
  }*/
  
  //Gestion des LEDS
  if (Serial.available()>0) {
      message = Serial.read() - '0';   
      //Serial.println("Serial = " + String(Serial.read()) + "Message = " + String(message));
  }
  if(Abs(analogRead(0)-MoyANA1)>10||Abs(analogRead(1)-MoyANA2)>10)
  { 
    message = 2;
    Serial.println(1,DEC);
    delay(50);
    FDeb = true; 
  }  
  
  if(message !=0)
  {
    switch (message){
      case 1:
        RAZ();
        break;
      case 2:
        
        if(FDeb == true)
        {
          //Allume les LEDs
          FDeb = false;
          for(i=2; i<=7; i++)
          {
            digitalWrite (i, HIGH);
            y=2;
          }
        }  
        //Commence le chenillard
        //param : duree total du chenillard(en millisecond)
        //chenillard(1000);
        break;
      case 100:
        FIN();
        message = 1;
        break;
      default:
        Serial.println("Serial OK - RIEN");
        break;
    }
  }  
}



void CapteurAnalog1(){
  //TabANA1[j] = analogRead(0);
  //j++;
  //MoyANA1 = 0;
  //for (short i = 0; i < 10; i++) 
  //{
    MoyANA1 = analogRead(0); 
    //Serial.println(MoyANA1);   
  //}
   //MoyANA1 = MoyANA1/10;
    
  //if(j > 10)
  //  j = 0;
}

void CapteurAnalog2(){
  //TabANA2[j] = analogRead(1);
  //j++;
  //MoyANA2 = 0;
  //for (short i = 0; i < 10; i++) 
  //{
  //  MoyANA2 = MoyANA2 + TabANA2[i];  
  //}
  MoyANA2 = analogRead(1);
  //if(j > 10)
  //  j = 0;
}

void chenillard(int time)
{
  //Chenillard
  if( y < 8 ) {
    delay (time/nombreLED);
    digitalWrite (y, LOW); // éteint la DEL
    y++;
  }
}
  
void RAZ()
{
  //Eteint les LEDs
  for (byte i = 2 ; i <= 7 ; i++) {
    digitalWrite (i, LOW);
  }
}

void FIN()
{ 
  //Clignotement 3 fois
  //Clignotement 1
  for (i = 2; i <= 7; i++){
    digitalWrite (i, HIGH);    
  }
  delay(1000);
  for (i = 2; i <= 7; i++){
    digitalWrite (i, LOW);    
  }
  delay(1000);
  
  //Clignotement 2
  for (i = 2; i <= 7; i++){
    digitalWrite (i, HIGH);    
  }
  delay(1000);
  for (i = 2; i <= 7; i++){
    digitalWrite (i, LOW);    
  }
  delay(1000);
  
  //Clignotement 3
  for (i = 2; i <= 7; i++){
    digitalWrite (i, HIGH);    
  }
  delay(1000);
  for (i = 2; i <= 7; i++){
    digitalWrite (i, LOW);    
  }
  delay(1000);
}

short Abs(short a){
  if(a<0)
   a =-a;

   return a;  
}
