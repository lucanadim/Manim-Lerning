from manim import *

class Day6(Scene):
    def construct(self):
        text1 = Text("Koordinaten System erklärung").scale(0.7).shift(UP*3.5, LEFT*3.7)
        text2_1 = MathTex("y = x", color=BLUE).scale(1.4).shift(UP*2, LEFT*4)
        text2_2 = MathTex("y = x^2", color=BLUE).scale(1.4).shift(UP*2, LEFT*4)
        text2_3 = MathTex("y = x^2 + 2", color=BLUE).scale(1.4).shift(UP*2, LEFT*4)
        text2_4 = MathTex("y = x^2 -2", color=BLUE).scale(1.4).shift(UP*2, LEFT*4)
        text2_5 = MathTex("y = x^2", color=BLUE).scale(1.4).shift(UP*2, LEFT*4)

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
        punkt1_3 = Dot(axes2.c2p(1,3), color=BLUE)
        punkt1_4 = Dot(axes2.c2p(1,-1), color=BLUE)
        punkt1_5 = Dot(axes2.c2p(1,1), color=BLUE)

        punkt_lable1_1 = MathTex("(1,1)", color=BLUE).next_to(punkt1_1, RIGHT)
        punkt_lable1_2 = MathTex("(1,1)", color=BLUE).next_to(punkt1_2, RIGHT)
        punkt_lable1_3 = MathTex("(1,3)", color=BLUE).next_to(punkt1_3, RIGHT)
        punkt_lable1_4 = MathTex("(1,-1)", color=BLUE).next_to(punkt1_4, RIGHT)
        punkt_lable1_5 = MathTex("(1,-1)", color=BLUE).next_to(punkt1_5, RIGHT)

        graph1_1 = axes1.plot(lambda x: x, color=BLUE)
        graph1_2 = axes2.plot(lambda x: x**2, color=BLUE)
        graph1_3 = axes2.plot(lambda x: x**2 + 2, color=BLUE)
        graph1_4 = axes2.plot(lambda x: x**2 - 2, color=BLUE)
        graph1_5 = axes2.plot(lambda x: x**2, color=BLUE)

        self.play(Write(text1), run_time=0.7)
        self.play(Write(text2_1))
        self.play(Create(axes1))
        self.wait()
        self.play(Write(graph1_1))
        self.play(Create(punkt1_1))
        self.play(Write(punkt_lable1_1))
        self.wait()
        self.play(
            Transform(text2_1, text2_2),
            Transform(punkt1_1, punkt1_2),
            Transform(punkt_lable1_1, punkt_lable1_2),
            Transform(graph1_1, graph1_2),
            Transform(axes1, axes2),
            )
        self.wait(2)
        self.play(
            Transform(text2_1, text2_3),
            Transform(punkt1_1, punkt1_3),
            Transform(punkt_lable1_1, punkt_lable1_3),
            Transform(graph1_1, graph1_3),
        )
        self.wait()
        self.play(
            Transform(text2_1, text2_4),
            Transform(punkt1_1, punkt1_4),
            Transform(punkt_lable1_1, punkt_lable1_4),
            Transform(graph1_1, graph1_4),
        )
        self.wait()
        self.play(
            Transform(text2_1, text2_5),
            Transform(punkt1_1, punkt1_5),
            Transform(punkt_lable1_1, punkt_lable1_5),
            Transform(graph1_1, graph1_5),
        )
        self.wait()
