Boid boid;

void setup() {
    size(800, 800); 
    smooth();
    noStroke();
    boid = new Boid(width/2, height/2, 0.05);
    background(51);
}

void draw() { 
    fill(51, 63);
    rect(0, 0, width, height);
    boid.setTarget(cx, cy);
    boid.update();
    boid.show();
}

class Boid {
    private float t = random(1.0);
    private float x = 0;
    private float y = 0;
    private float tgX = 0;
    private float tgY = 0;
    private float easing = 0.25;
    private float wiggleRad = 3.0;
    private int sz = 50;

    Boid(float _x, float _y) {
        x = _x;
        y = _y;
    }

    Boid(float _x, float _y, float _easing) {
        x = _x;
        y = _y;
        easing = _easing;
    }

    void show() {
        noStroke();
        fill(255, 255, 255);
        ellipse(x, y, sz, sz);
    }

    void update() {
        float dx = tgX - x;
        this.x += dx * this.easing;
        this.x += noise(t)*wiggleRad*2 - wiggleRad;

        float dy = tgY - y;
        this.y += dy * this.easing;
        this.y += noise(t + 100)*wiggleRad*2 - wiggleRad;

        this.x = constrain(this.x, sz, width-sz);
        this.y =  constrain(this.y, sz, height-sz);

        t += 0.01;
    }

    void setTarget(float _tgX, float _tgY) {
        this.tgX = _tgX;
        this.tgY = _tgY;
    }

    void setWiggleRadius(float r) {
        this.wiggleRad = r;
    }
}
