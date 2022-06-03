% rebase('layout.tpl', title=title, menu=menu, year=year)
<div class="container col-md-4 col-md-offset-4" style="margin: 0 auto; width:80%;">
    <br>
    <div class="accordion" id="accordionExample">
        <div class="accordion-item">
            <h2 class="accordion-header" id="headingOne">
            <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne"
            aria-expanded="true" aria-controls="collapseOne">
            Описание работы Алгоритма Гамильтона
            </button>
            </h2>
            <div id="collapseOne" class="accordion-collapse collapse show" aria-labelledby="headingOne"
                data-bs-parent="#accordionExample" style="">
                <div class="accordion-body">
                    <div class="row" style="text-indent: 30px">
                        <div class="col align-self-center">
                            <img height="auto" width="90%" src="https://imgur.com/uxdvoEO.png">
                        </div>
                        <div class="col">
                            <div class="row">
                                <p>
                                    Простой цикл, проходящий через все вершины графа, называется <strong>гамильтоновым</strong>. Простая цепь, проходящий через все вершины графа, называется гамильтоновой. Также с гамильтоновым графом тесно связано понятие <strong>гамильтонова пути</strong>, который является простым путём (путём без петель), проходящим через каждую вершину графа <code>ровно один раз</code>.
                                </p>
                            </div>
                            <div class="row">
                                <p>
                                    Гамильтонов путь отличается от цикла тем, что у пути начальные и конечные точки могут не совпадать. <code>Гамильтонов цикл является гамильтоновым путём</code>. Задача нахождения гамильтоновых циклов получила свое развитие в связи с рядом практических задач, одной из которых является так называемая <strong>задача коммивояжера</strong>.
                                </p>
                            </div>
                        </div>
                    </div>
                    <div class="row" style="text-indent: 30px">
                        <div class="col">
                            <div class="row">
                                <p>
                                    <strong>Задача коммивояжёра</strong> — одна из самых известных задач комбинаторной оптимизации, <code>заключающаяся в поиске самого выгодного маршрута</code>, проходящего через указанные города хотя бы по одному разу с последующим возвратом в исходный город. В условиях задачи указываются критерий выгодности маршрута (кратчайший, самый дешёвый, совокупный критерий и тому подобное) и соответствующие матрицы расстояний, стоимости и тому подобного. Как правило, указывается, что маршрут должен проходить через каждый город <code>только один раз</code> — в таком случае выбор осуществляется среди гамильтоновых циклов.
                                </p>
                            </div>
                            <div class="row">
                                <p>
                                    В отличие от поиска <strong>эйлеровых циклов, проходящих через каждое ребро графа по одному разу</strong>, где еще Эйлером получено необходимое и достаточное условие существования цикла, для гамильтоновых циклов такого условия не найдено. Существуют, однако, достаточные условия существования гамильтоновых циклов.
                                </p>
                            </div>
                        </div>
                    </div>
                    <div class="row" style="text-indent: 30px">
                        <div class="col align-self-center">
                            <img height="auto" width="90%" src="https://imgur.com/QcOUB32.png">
                        </div>
                        <div class="col">
                            <div class="row">
                                <p>
                                    <strong>Гамильтоновы путь, цикл и граф</strong> названы в честь ирландского математика <code>У. Гамильтона</code>, который впервые определил эти классы, исследовав задачу «кругосветного путешествия» по додекаэдру. В этой задаче вершины додекаэдра символизировали известные города, такие как <code>Брюссель, Амстердам, Эдинбург, Пекин, Прага, Дели, Франкфурт и др.</code>, а рёбра — <code>соединяющие их дороги</code>.
                                </p>
                            </div>
                            <div class="row">
                                <p>
                                    Путешествующий должен пройти «вокруг света», найдя путь, который проходит через все вершины <code>ровно один раз</code>. Чтобы сделать задачу более интересной, порядок прохождения городов устанавливался заранее. А чтобы было легче запомнить, какие города уже соединены, в каждую вершину додекаэдра был вбит гвоздь, и проложенный путь отмечался небольшой верёвкой, которая могла обматываться вокруг гвоздя.
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <br>
    <form onsubmit="return onSubmitMatrix();">
        <table id="matrix" align="center">
        <tbody></tbody>
    </table>
    <fieldset>
        <div class="form-group">
            <label class="form-label mt-4">Размерность матрицы смежности</label>
            <div class="form-group">
                <div class="input-group mb-3">
                    <input type="number" class="form-control r" id="input-size"
                    value="3" 
                    placeholder="Введите размерность"
                    aria-describedby="button-update"
                    onkeypress="return isNumberKey(event)"
                    min="0">
                    <button class="btn btn-primary" type="button" id="button-update">Обновить</button>
                </div>
            </div>
        </div>
        <br>
        <button type="submit" class="btn btn-primary">Найти цикл</button>
    </fieldset>

</form>
<div id="result-table">
</div>
</div>