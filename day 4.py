from manim import *

class Day4(Scene):
    def construct(self):
        text1 = Text("Parabel Standards").shift(UP*3.5).scale(0.8)
        text2 = Text("der parabel nullpunkt wird um 2 stellen auf der y achse nach oben verschoben").scale(0.6).shift(DOWN*3)
        text2.add_background_rectangle(color=BLACK)
        text3 = Text("auf der ersten x koordinate (1,0) schneidet sich die parabel\nauf der vierten y koordinate (0,4) das heißt der schnitpunkt ist\n(1,0) + (0,4) = (1,4)").scale(0.6).shift(DOWN*3)
        text3.add_background_rectangle(color=BLACK)

        axes1 = Axes(
            x_range=[-5, 5, 1],
            y_range=[-3, 10, 1],
            x_length=8,
            y_length=7,
            axis_config={"include_numbers": True}
        ).shift(DOWN * 0.35)

        parabola1 = axes1.plot(lambda x: x**2, color=BLUE)
        parabola2 = axes1.plot(lambda x: x**2 + 2, color=ORANGE)
        parabula3 = axes1.plot(lambda x: 4*x**2, color=YELLOW)

        lable1 = axes1.get_graph_label(parabola1, label="y = x^2")
        lable2 = axes1.get_graph_label(parabola2, label="y = x^2 + 2")
        lable3 = axes1.get_graph_label(parabula3, label="y = 4x^2")

        punkt1 = Dot(color=RED).next_to(lable2)
        punkt2 = Dot(axes1.c2p(0,2), color=RED)
        punkt3 = Dot(axes1.c2p(1,4), color=RED)
        punkt4 = Dot(axes1.c2p(1,0), color=RED)
        punkt5 = Dot(axes1.c2p(0,4), color=RED)
        punkt6 = Dot(axes1.c2p(3,9), color=RED).shift(RIGHT*0.26, UP*0.3)

        punkt_lable1 = MathTex("(1,4)").next_to(punkt3, UP)
        punkt_lable2 = MathTex("(1,0)").next_to(punkt4, UP)
        punkt_lable3 = MathTex("(0,4)").next_to(punkt5, LEFT)

        linie1 = Line(punkt5.get_center(), punkt3.get_center(), color=RED)
        linie2 = Line(punkt3.get_center(), punkt4.get_center(), color=RED)

        pfeil1 = Arrow(punkt1.get_center(), punkt2.get_center(), color=RED)
        pfeil2 = Arrow(punkt6.get_center(), punkt3.get_center(), color=RED)

        self.play(Write(text1))
        self.play(Create(axes1))
        self.play(Create(parabola1), Write(lable1))
        self.wait()
        self.play(Transform(parabola1, parabola2), Transform(lable1, lable2), run_time=1.5)
        self.play(FadeIn(punkt1), FadeIn(punkt2))
        self.play(Create(pfeil1))
        self.play(Write(text2))
        self.wait(2)
        self.play(Uncreate(pfeil1))
        self.play(Unwrite(text2))
        self.play(FadeOut(punkt1), FadeOut(punkt2))
        self.wait()
        self.play(Transform(parabola1, parabula3), Transform(lable1, lable3), run_time=1.5)
        self.play(FadeIn(punkt3), FadeIn(punkt4), FadeIn(punkt5))
        self.play(Write(punkt_lable1), Write(punkt_lable2), Write(punkt_lable3))
        self.play(Create(linie1))
        self.play(Create(linie2))
        self.play(FadeIn(punkt6))
        self.play(Create(pfeil2))
        self.play(Write(text3))
        self.wait(5)
        self.play(Unwrite(text3), Uncreate(pfeil2))
        self.play(Uncreate(linie2))
        self.play(Uncreate(linie1))
        self.play(FadeOut(punkt6), FadeOut(punkt5), FadeOut(punkt4), FadeOut(punkt3), Unwrite(punkt_lable1), Unwrite(punkt_lable2), Unwrite(punkt_lable3))
        self.wait()
        self.play(Uncreate(parabola1), Unwrite(lable1))
        self.play(Uncreate(axes1))
        self.wait()
