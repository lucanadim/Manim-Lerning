from manim import *

class day10(Scene):
    def construct(self):
        text1_1 = Text("Parabel aufbau").scale(0.7).shift(UP*3.5, LEFT*5.3)
        text2_1 = MathTex("y = x", color=BLUE).scale(1.4).shift(UP*2, LEFT*5.2)
        text2_2 = MathTex("y = x^2", color=BLUE).scale(1.4).shift(UP*2, LEFT*5.2)

        axes1 = Axes(
            x_range=[-7, 7, 1],
            y_range=[-7, 7, 1],
            x_length=7,
            y_length=7,
            axis_config={"include_numbers": True}
        ).shift(DOWN * 0.1)

        axes2 = Axes(
            x_range=[-7, 7, 1],
            y_range=[-3, 10, 1],
            x_length=8,
            y_length=7,
            axis_config={"include_numbers": True}
        ).shift(DOWN * 0.1)

        punkt1_1 = Dot(axes1.c2p(1,1), color=BLUE)
        punkt1_2 = Dot(axes2.c2p(1,1), color=BLUE)

        punkt_lable1_1 = MathTex("(1,1)", color=BLUE).next_to(punkt1_1, RIGHT)
        punkt_lable1_2 = MathTex("(1,1)", color=BLUE).next_to(punkt1_2, RIGHT)

        graph1_1 = axes1.plot(lambda x: x, color=BLUE)
        graph1_2 = axes2.plot(lambda x: x**2, color=BLUE)

        self.play(Write(text1_1))
        self.play(Write(text2_1))
        self.play(Create(axes1))
        self.play(Create(graph1_1))
        self.play(Create(punkt1_1))
        self.play(Write(punkt_lable1_1))
        self.wait(2)
        self.play(
            Transform(text2_1, text2_2),
            Transform(axes1, axes2),
            Transform(graph1_1, graph1_2),
            Transform(punkt1_1, punkt1_2),
            Transform(punkt_lable1_1, punkt_lable1_2),
        )
        self.wait()