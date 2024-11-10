import logging
import unittest
import rt_with_exceptions as runner


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @classmethod
    def setUpClass(cls):
        logging.basicConfig(filename='runner_tests.log', filemode='w', level=logging.INFO, encoding='utf-8',
                            format='%(asctime)s | %(levelname)s | %(message)s')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            rn = runner.Runner(name='Бегунъ', speed=-100)
            for _ in range(10):
                rn.walk()
            self.assertEqual(rn.distance, 50)
        except ValueError:
            logging.warning(msg='Неверная скорость для Runner')
        logging.info('Тест "test_walk" выполнен успешно')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):

        try:
            rn = runner.Runner(name=7, speed=7)
            for _ in range(10):
                rn.run()
            self.assertEqual(rn.distance, 100)
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner')
        logging.info('Тест "test_run" выполнен успешно')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):

        r1 = runner.Runner(name='Anton')
        r2 = runner.Runner(name='Denis')
        for _ in range(10):
            r1.run()
            r2.walk()
        self.assertNotEqual(r1.distance, r2.distance)


if __name__ == '__main__':
    unittest.main()
