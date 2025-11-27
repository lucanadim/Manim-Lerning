from manim import *

class demo(Scene):
    def construct(self):
        t = Text ("hello i am luca").shift(UP)
        t2 = Tex ("Drawing Text").shift(DOWN)
        self.play(Write(t), Write(t2))
        self.wait(1)
        self.play(FadeOut(t), FadeOut(t2))
        
        self.wait(1)
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)
        square = Square()
        square.set_fill(BLUE, opacity=0.5)

        t3 = Text ("Drawing a circle and square")
        t3.next_to(circle, UP, buff=0.5)
        self.play(Write(t3))
        circle.next_to(square, LEFT, buff=0.5)
        square.next_to(circle, RIGHT, buff=3)
        self.play(Create(circle), Create(square))
        self.play(FadeOut(circle, square, t3))
        self.wait(1)

        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)
        

        square = Square()
        square.rotate(PI / 4)

        t4 = Text ("transform between a circle and a square")
        t4.next_to(circle, UP, buff=0.5)

        self.play(Write(t4))
        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))
        self.play(FadeOut(t4))

        circle = Circle()
        square = Square()
        triangle = Triangle()

        circle.shift(LEFT)
        square.shift(UP)
        triangle.shift(RIGHT)

        self.add(circle, square, triangle)
        self.wait(1)
        self.play(FadeOut(circle, square, triangle))