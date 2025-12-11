from manim import *

class day10(Scene):
    def construct(self):
        text1_1 = Text("Parabel aufbau").scale(0.7).shift(UP*3.5, LEFT*5.3)
        text2_1 = MathTex("y = x", color=BLUE).scale(1.4).shift(UP*2, LEFT*5.2)
        text2_2 = MathTex("y = x^2", color=BLUE).scale(1.4).shift(UP*2, LEFT*5.2)
        text2_3 = MathTex("y = x^2 + 2", color=BLUE).scale(1.4).shift(UP*2, LEFT*5)
        text2_4 = MathTex("y = x^2 - 2", color=BLUE).scale(1.4).shift(UP*2, LEFT*5)
        text2_5 = MathTex("y = x^2", color=BLUE).scale(1.4).shift(UP*2, LEFT*5.2)
        text2_6 = MathTex("y = (x-3)^2", color=BLUE).scale(1.4).shift(UP*2, LEFT*5)
        text2_7 = MathTex("y = (x+3)^2", color=BLUE).scale(1.4).shift(UP*2, LEFT*5)
        text2_8 = MathTex("y = x^2", color=BLUE).scale(1.4).shift(UP*2, LEFT*5.2)
        text3_1 = Text("der Graph y = x² wir Parabel genant. \nEr ist eine Linie bei der die y Koordinaten \nden x Koordinaten entsprechen aber diese \nim quadrat stehen.").scale(0.5).shift(RIGHT*3).add_background_rectangle(color=BLACK)
        text3_2 = Text("Bei der adition oder suptraktion hinter dem x \nwir die Parabel auf der y achse nach oben \noder unten verschoben.").scale(0.5).shift(UP, RIGHT*3).add_background_rectangle(color=BLACK)
        text3_3 = Text("Wenn man das x in Klammern setzt und dahinter \ndas adiren oder suptrahieren macht dann wird \ndie Parabel nach link oder rechts \nim Koordinatensystem verschoben.\nWICHTIG --> alles was Plus gerechnet wird geht \nin den minus bereich (nach Links) \nund alles was Minus gerechnet wird geht \nin den plus bereich (nach Rechts).").scale(0.5).shift(RIGHT*3, UP*2).add_background_rectangle(color=BLACK)
        text3_4 = Text("Mit diesen Regeln können wir die Parabel \nan jede Position des Koordinatensystems \nverschieben die wir möchten").scale(0.5).shift(RIGHT*3).add_background_rectangle(color=BLACK)

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
        ).shift(DOWN * 0.1, LEFT * 2)

        punkt1_1 = Dot(axes1.c2p(1,1), color=BLUE)
        punkt1_2 = Dot(axes2.c2p(1,1), color=BLUE)
        punkt1_3 = Dot(axes2.c2p(1,3), color=BLUE)
        punkt1_4 = Dot(axes2.c2p(1,-1), color=BLUE)
        punkt1_5 = Dot(axes2.c2p(1,1), color=BLUE)
        punkt1_6 = Dot(axes2.c2p(4,1), color=BLUE)
        punkt1_7 = Dot(axes2.c2p(-2,1), color=BLUE)
        punkt1_8 = Dot(axes2.c2p(1,1), color=BLUE)

        punkt_lable1_1 = MathTex("(1,1)", color=BLUE).next_to(punkt1_1, RIGHT)
        punkt_lable1_2 = MathTex("(1,1)", color=BLUE).next_to(punkt1_2, RIGHT)
        punkt_lable1_3 = MathTex("(1,3)", color=BLUE).next_to(punkt1_3, RIGHT)
        punkt_lable1_4 = MathTex("(1,-1)", color=BLUE).next_to(punkt1_4, RIGHT)
        punkt_lable1_5 = MathTex("(1,1)", color=BLUE).next_to(punkt1_5, RIGHT)
        punkt_lable1_6 = MathTex("(4,1)", color=BLUE).next_to(punkt1_6, RIGHT)
        punkt_lable1_7 = MathTex("(-2,1)", color=BLUE).next_to(punkt1_7, RIGHT)
        punkt_lable1_8 = MathTex("(1,1)", color=BLUE).next_to(punkt1_8, RIGHT)

        graph1_1 = axes1.plot(lambda x: x, color=BLUE)
        graph1_2 = axes2.plot(lambda x: x**2, color=BLUE)
        graph1_3 = axes2.plot(lambda x: x**2 + 2, color=BLUE)
        graph1_4 = axes2.plot(lambda x: x**2 - 2, color=BLUE)
        graph1_5 = axes2.plot(lambda x: x**2, color=BLUE)
        graph1_6 = axes2.plot(lambda x: (x-3)**2, color=BLUE)
        graph1_7 = axes2.plot(lambda x: (x+3)**2, color=BLUE)
        graph1_8 = axes2.plot(lambda x: x**2, color=BLUE)

        self.play(Write(text1_1))
        self.play(Write(text2_1))
        self.play(Create(axes1))
        self.play(Create(graph1_1))
        self.play(Create(punkt1_1))
        self.play(Write(punkt_lable1_1))
        self.wait(1)
        self.play(
            Transform(text2_1, text2_2),
            Transform(axes1, axes2),
            Transform(graph1_1, graph1_2),
            Transform(punkt1_1, punkt1_2),
            Transform(punkt_lable1_1, punkt_lable1_2),
        )
        self.play(Write(text3_1), run_time=4)
        self.wait(2)
        self.play(Unwrite(text3_1), run_time=2)
        self.play(
            Transform(text2_1, text2_3),
            Transform(graph1_1,graph1_3),
            Transform(punkt1_1, punkt1_3),
            Transform(punkt_lable1_1, punkt_lable1_3),
            run_time = 1.5
        )
        self.play(Write(text3_2), run_time=4)
        self.play(
            Transform(text2_1, text2_4),
            Transform(graph1_1, graph1_4),
            Transform(punkt1_1, punkt1_4),
            Transform(punkt_lable1_1, punkt_lable1_4),
            run_time = 1.5
        )
        self.wait()
        self.play(Unwrite(text3_2), run_time=2)
        self.play(
            Transform(text2_1, text2_5),
            Transform(graph1_1, graph1_5),
            Transform(punkt1_1, punkt1_5),
            Transform(punkt_lable1_1, punkt_lable1_5),
            run_time = 1.5
        )
        self.wait(2)
        self.play(
            Transform(text2_1, text2_6),
            Transform(graph1_1, graph1_6),
            Transform(punkt1_1, punkt1_6),
            Transform(punkt_lable1_1, punkt_lable1_6),
            run_time = 1.5
        )
        self.play(Write(text3_3), run_time=2)
        self.play(
            Transform(text2_1, text2_7),
            Transform(graph1_1, graph1_7),
            Transform(punkt1_1, punkt1_7),
            Transform(punkt_lable1_1, punkt_lable1_7),
            run_time = 1.5
        )
        self.wait(3)
        self.play(Unwrite(text3_3), run_time=2)
        self.play(
            Transform(text2_1, text2_8),
            Transform(graph1_1, graph1_8),
            Transform(punkt1_1, punkt1_8),
            Transform(punkt_lable1_1, punkt_lable1_8),
            run_time = 1.5
        )
        self.play(Write(text3_4), run_time=2)
        self.wait()
