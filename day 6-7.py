from manim import *

class Day6(Scene):
    def construct(self):
        text1 = Text("Koordinaten System erklärung").scale(0.7).shift(UP*3.5, LEFT*3.7)
        text2_1 = MathTex("y = x", color=BLUE).scale(1.4).shift(UP*2, LEFT*5.2)
        text2_2 = MathTex("y = x^2", color=BLUE).scale(1.4).shift(UP*2, LEFT*5.2)
        text2_3 = MathTex("y = x^2 + 2", color=BLUE).scale(1.4).shift(UP*2, LEFT*5.2)
        text2_4 = MathTex("y = x^2 - 2", color=BLUE).scale(1.4).shift(UP*2, LEFT*5.2)
        text2_5 = MathTex("y = x^2", color=BLUE).scale(1.4).shift(UP*2, LEFT*5.2)
        text2_6 = MathTex("y = -x^2", color=BLUE).scale(1.4).shift(UP*2, LEFT*5.2)
        text2_7 = MathTex("y = -x^2 + 5", color=BLUE).scale(1.4).shift(UP*2, LEFT*5.2)
        text2_8 = MathTex("y = x^2", color=BLUE).scale(1.4).shift(UP*2, LEFT*5.2)
        text2_9 = MathTex("y = 4x^2", color=BLUE).scale(1.4).shift(UP*2, LEFT*5.2)
        text2_10 = MathTex("y = 0.3x^2", color=BLUE).scale(1.4).shift(UP*2, LEFT*5.2)
        text2_11 = MathTex("y = x^2", color=ORANGE).scale(1.4).shift(UP*2, LEFT*5.2)
        text3 = Text("Ein paar Formel Beispiele \nin einem Koordinatensystem").scale(0.5).shift(DOWN*3.5, LEFT*4.8)

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

        axes3 = Axes(
            x_range=[-7, 7, 1],
            y_range=[-3, 10, 1],
            x_length=8,
            y_length=7,
            axis_config={"include_numbers": True}
        ).shift(DOWN * 1.4, LEFT*2).scale(0.7)

        tabelle1 = Table(
            table=[
                ["x", "-5", "-4", "-3", "-2", "-1", "0", "1", "2", "3", "4", "5"],
                ["y", "25", "16", "9", "4", "1", "0", "1", "4", "9", "16", "25"]
            ],
            element_to_mobject=lambda x: Text(str(x), font_size=32),
        ).scale(0.6).shift(UP * 2.5, RIGHT*1.3)

        punkt1_1 = Dot(axes1.c2p(1,1), color=BLUE)
        punkt1_2 = Dot(axes2.c2p(1,1), color=BLUE)
        punkt1_3 = Dot(axes2.c2p(1,3), color=BLUE)
        punkt1_4 = Dot(axes2.c2p(1,-1), color=BLUE)
        punkt1_5 = Dot(axes2.c2p(1,1), color=BLUE)
        punkt1_6 = Dot(axes2.c2p(1,-1), color=BLUE)
        punkt1_7 = Dot(axes2.c2p(1,4), color=BLUE)
        punkt1_8 = Dot(axes2.c2p(1,1), color=BLUE)
        punkt1_9 = Dot(axes2.c2p(1,4), color=BLUE)
        punkt1_10 = Dot(axes2.c2p(1,0.3), color=BLUE)
        punkt2_1 = Dot(axes3.c2p(1,1), color=ORANGE)
        punkt2_2 = Dot(axes3.c2p(-1,1), color=ORANGE)
        punkt2_3 = Dot(axes3.c2p(-2,4), color=ORANGE)
        punkt2_4 = Dot(axes3.c2p(2,4), color=ORANGE)
        punkt2_5 = Dot(axes3.c2p(-3,9), color=ORANGE)
        punkt2_6 = Dot(axes3.c2p(3,9), color=ORANGE)
        punkt3_1 = Dot(color=ORANGE).next_to(tabelle1, DOWN).shift(UP*0.2, LEFT*0.35)
        punkt3_2 = Dot(color=ORANGE).next_to(tabelle1, DOWN).shift(UP*0.2, RIGHT*1.5)
        punkt3_3 = Dot(color=ORANGE).next_to(tabelle1, DOWN).shift(UP*0.2, LEFT*1.33)
        punkt3_4 = Dot(color=ORANGE).next_to(tabelle1, DOWN).shift(UP*0.2, RIGHT*2.4)
        

        punkt_lable1_1 = MathTex("(1,1)", color=BLUE).next_to(punkt1_1, RIGHT)
        punkt_lable1_2 = MathTex("(1,1)", color=BLUE).next_to(punkt1_2, RIGHT)
        punkt_lable1_3 = MathTex("(1,3)", color=BLUE).next_to(punkt1_3, RIGHT)
        punkt_lable1_4 = MathTex("(1,-1)", color=BLUE).next_to(punkt1_4, RIGHT)
        punkt_lable1_5 = MathTex("(1,1)", color=BLUE).next_to(punkt1_5, RIGHT)
        punkt_lable1_6 = MathTex("(1,-1)", color=BLUE).next_to(punkt1_6, RIGHT)
        punkt_lable1_7 = MathTex("(1,4)", color=BLUE).next_to(punkt1_7, RIGHT)
        punkt_lable1_8 = MathTex("(1,1)", color=BLUE).next_to(punkt1_8, RIGHT)
        punkt_lable1_9 = MathTex("(1,4)", color=BLUE).next_to(punkt1_9, RIGHT)
        punkt_lable1_10 = MathTex("(1,0.3)", color=BLUE).next_to(punkt1_10, RIGHT)
        punkt_lable2_1 = MathTex("(1,1)", color=ORANGE).next_to(punkt2_1, RIGHT)
        punkt_lable2_2 = MathTex("(-1,1)", color=ORANGE).next_to(punkt2_2, LEFT)
        punkt_lable2_3 = MathTex("(-2,4)", color=ORANGE).next_to(punkt2_3, LEFT)
        punkt_lable2_4 = MathTex("(2,4)", color=ORANGE).next_to(punkt2_4, RIGHT)
        punkt_lable2_5 = MathTex("(-3,9)", color=ORANGE).next_to(punkt2_5, LEFT)
        punkt_lable2_6 = MathTex("(3,9)", color=ORANGE).next_to(punkt2_6, RIGHT)

        graph1_1 = axes1.plot(lambda x: x, color=BLUE)
        graph1_2 = axes2.plot(lambda x: x**2, color=BLUE)
        graph1_3 = axes2.plot(lambda x: x**2 + 2, color=BLUE)
        graph1_4 = axes2.plot(lambda x: x**2 - 2, color=BLUE)
        graph1_5 = axes2.plot(lambda x: x**2, color=BLUE)
        graph1_6 = axes2.plot(lambda x: -x**2, color=BLUE)
        graph1_7 = axes2.plot(lambda x: -x**2 + 5, color=BLUE)
        graph1_8 = axes2.plot(lambda x: x**2, color=BLUE)
        graph1_9 = axes2.plot(lambda x: 4*x**2, color=BLUE)
        graph1_10 = axes2.plot(lambda x: 0.3*x**2, color=BLUE)
        graph2_1 = axes3.plot(lambda x: x**2, color=ORANGE)

        #Animation----------------------------------------------------------------------

        self.play(Write(text1), run_time=0.7)
        self.play(Write(text3), run_time=0.7)
        self.play(Write(text2_1))
        self.play(Create(axes1))
        self.wait()
        self.play(Write(graph1_1))
        self.play(Create(punkt1_1))
        self.play(Write(punkt_lable1_1))
        self.wait(2)
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
        self.wait(2)
        self.play(
            Transform(text2_1, text2_5),
            Transform(punkt1_1, punkt1_5),
            Transform(punkt_lable1_1, punkt_lable1_5),
            Transform(graph1_1, graph1_5),
        )
        self.wait(2)
        self.play(
            Transform(text2_1, text2_6),
            Transform(punkt1_1, punkt1_6),
            Transform(punkt_lable1_1, punkt_lable1_6),
            Transform(graph1_1, graph1_6),
        )
        self.wait()
        self.play(
            Transform(text2_1, text2_7),
            Transform(punkt1_1, punkt1_7),
            Transform(punkt_lable1_1, punkt_lable1_7),
            Transform(graph1_1, graph1_7),
        )
        self.wait()
        self.play(
            Transform(text2_1, text2_8),
            Transform(punkt1_1, punkt1_8),
            Transform(punkt_lable1_1, punkt_lable1_8),
            Transform(graph1_1, graph1_8),
        )
        self.wait(2)
        self.play(
            Transform(text2_1, text2_9),
            Transform(punkt1_1, punkt1_9),
            Transform(punkt_lable1_1, punkt_lable1_9),
            Transform(graph1_1, graph1_9),
        )
        self.wait(2)
        self.play(
            Transform(text2_1, text2_10),
            Transform(punkt1_1, punkt1_10),
            Transform(punkt_lable1_1, punkt_lable1_10),
            Transform(graph1_1, graph1_10),
        )
        self.wait(2)
        self.play(Unwrite(text3))
        self.play(
            Transform(text2_1, text2_11),
            Transform(punkt1_1, punkt2_1),
            Transform(punkt_lable1_1, punkt_lable2_1),
            Transform(graph1_1, graph2_1),
            Transform(axes1, axes3),
        )
        self.wait(2)
        self.play(
            Create(punkt2_2),
            Create(punkt_lable2_2),
            Create(punkt2_3),
            Create(punkt_lable2_3),
            Create(punkt2_4),
            Create(punkt_lable2_4),
            Create(punkt2_5),
            Create(punkt_lable2_5),
            Create(punkt2_6),
            Create(punkt_lable2_6),
            run_time=0.5
        )
        self.play(Create(tabelle1))
        self.wait(2)
        self.play(Create(punkt3_1), run_time=0.3)
        self.play(Create(punkt3_2), run_time=0.3)
        self.play(Create(punkt3_3), run_time=0.3)
        self.play(Create(punkt3_4), run_time=0.3)
        self.wait(2)
