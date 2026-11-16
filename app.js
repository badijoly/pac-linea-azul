/**
 * Dashboard de Evaluación Línea Azul · PAC 2026
 * Con datos normalizados a escala 0.0 a 5.0 y módulo comparativo transversal con Línea Verde
 */

let RAW_DATA = null;
let CURRENT_HITO = 'Global'; // 'Global', 'Challwa', 'Desierto'
let ACTIVE_TAB = 'resumen';   // 'resumen', 'establecimientos'
let CHARTS = {};

// Fallback embedded data for file:// protocol support
const EMBEDDED_FALLBACK = {
  "metadata": {
    "programa": "Programa de Acción Climática (PAC 2026)",
    "linea": "Línea Azul",
    "escala_normalizada": "0 a 5.0 puntos"
  },
  "resumen_linea_azul": {
    "total_estudiantes": 76,
    "total_evaluaciones_pareadas": 132,
    "evaluaciones_challwa": 67,
    "evaluaciones_desierto_azul": 65,
    "estudiantes_evaluados_climatón": 43,
    "tasa_favorable_global": 91.7,
    "mejoraron_global": 89,
    "mantuvieron_global": 32,
    "retrocedieron_global": 11,
    "puntaje_pre_norm5": 2.34,
    "puntaje_post_norm5": 3.40,
    "delta_norm5": 1.07,
    "hake_global": 0.412,
    "challwa": {
      "n": 67,
      "mejoraron": 51,
      "mantuvieron": 10,
      "retrocedieron": 6,
      "tasa_favorable": 91.0,
      "pre_raw_9": 3.28,
      "post_raw_9": 5.55,
      "pre_norm5": 1.83,
      "post_norm5": 3.08,
      "delta_norm5": 1.26,
      "hake": 0.381,
      "preguntas": [
        {"id": "Q1", "enunciado": "Rol trófico de depredadores marinos", "pre_pct": 56.7, "post_pct": 71.6, "delta_pct": 14.9},
        {"id": "Q2", "enunciado": "Conservación de tiburones y rayas locales", "pre_pct": 17.9, "post_pct": 70.1, "delta_pct": 52.2},
        {"id": "Q3", "enunciado": "Equilibrio ecosistémico costero", "pre_pct": 22.4, "post_pct": 73.1, "delta_pct": 50.7}
      ]
    },
    "desierto_azul": {
      "n": 65,
      "mejoraron": 38,
      "mantuvieron": 22,
      "retrocedieron": 5,
      "tasa_favorable": 92.3,
      "pre_raw_4": 2.29,
      "post_raw_4": 2.98,
      "pre_norm5": 2.87,
      "post_norm5": 3.73,
      "delta_norm5": 0.87,
      "hake": 0.447,
      "preguntas": [
        {"id": "Q1", "enunciado": "Impacto de plásticos y microplásticos", "pre_pct": 53.0, "post_pct": 60.6, "delta_pct": 7.6},
        {"id": "Q2", "enunciado": "Vector de contaminación litoral de Antofagasta", "pre_pct": 62.1, "post_pct": 72.7, "delta_pct": 10.6},
        {"id": "Q3", "enunciado": "Manejo y prevención comunitaria de residuos", "pre_pct": 93.9, "post_pct": 90.9, "delta_pct": -3.0},
        {"id": "Colillas", "enunciado": "Identificación de colillas como residuo tóxico crítico", "pre_pct": 25.8, "post_pct": 69.7, "delta_pct": 43.9}
      ]
    }
  },
  "comparativa_lineas": {
    "linea_verde": {
      "establecimientos": 7,
      "estudiantes_unicos": 67,
      "evaluaciones_totales": 127,
      "tasa_favorable_global": 79.5,
      "pre_promedio_norm5": 3.26,
      "post_promedio_norm5": 3.71,
      "delta_promedio_norm5": 0.45,
      "hake_global": 0.214,
      "foco_tematico": "Humedales costeros, aves nativas, atmósfera y cielos oscuros"
    },
    "linea_azul": {
      "establecimientos": 8,
      "estudiantes_unicos": 76,
      "evaluaciones_totales": 132,
      "tasa_favorable_global": 91.7,
      "pre_promedio_norm5": 2.34,
      "post_promedio_norm5": 3.40,
      "delta_promedio_norm5": 1.07,
      "hake_global": 0.412,
      "foco_tematico": "Océano, biodiversidad de condrictios/tiburones, plásticos y colillas"
    },
    "total_pac_consolidado": {
      "establecimientos": 15,
      "estudiantes_unicos": 143,
      "evaluaciones_totales": 259,
      "tasa_favorable_ponderada": 85.7,
      "pre_promedio_norm5": 2.79,
      "post_promedio_norm5": 3.55,
      "delta_promedio_norm5": 0.76,
      "hake_ponderado": 0.315
    }
  }
};

const SCHOOLS_DIRECTORY = {
  "Escuela Claudio Matte Pérez": {
    dependencia: "Municipal (SLEP / CMDS)",
    sncae: "Sin Certificación",
    docente: "Equipo Docente Línea Azul",
    n_evals: 20,
    pre_norm5: 1.62,
    post_norm5: 3.25,
    delta_norm5: 1.63,
    pct_fav: 100.0,
    mej: 17,
    man: 3,
    ret: 0,
    hake: 0.500,
    climaton: "8 estudiantes evaluados (100% favorable)",
    recomendaciones: "Felicitar al equipo por alcanzar 100% de tasa favorable. Se sugiere dar continuidad profundizando en la clasificación de aves marinas que interactúan con los ecosistemas de tiburones costeros."
  },
  "Escuela Ecológica Humberto González Echegoyen": {
    dependencia: "Municipal (SLEP / CMDS)",
    sncae: "Sello Ecológico / Certificación Vigente (MMA)",
    docente: "Equipo Docente Línea Azul",
    n_evals: 17,
    pre_norm5: 3.18,
    post_norm5: 3.48,
    delta_norm5: 0.30,
    pct_fav: 76.5,
    mej: 5,
    man: 8,
    ret: 4,
    hake: 0.054,
    climaton: "10 estudiantes evaluados (100% favorable)",
    recomendaciones: "Comunidad con alto conocimiento basal previo (3.18 PRE). El menor delta responde al efecto techo. Se recomienda desafiar al grupo con proyectos aplicados de reducción de colillas y microplásticos en playas aledañas."
  },
  "Escuela Ecológica Padre Alberto Hurtado": {
    dependencia: "Municipal (SLEP / CMDS)",
    sncae: "Sello Ecológico / Certificación Vigente (MMA)",
    docente: "Equipo Docente Línea Azul",
    n_evals: 12,
    pre_norm5: 2.65,
    post_norm5: 3.92,
    delta_norm5: 1.27,
    pct_fav: 100.0,
    mej: 8,
    man: 4,
    ret: 0,
    hake: 0.466,
    climaton: "No participó en Climatón",
    recomendaciones: "Rendimiento sobresaliente (3.92 POST normalizado). Excelente apropiación del rol de los tiburones en la cadena trófica. Promover que los alumnos lideren brigadas de concientización en sus escuelas."
  },
  "Escuela Javiera Carrera": {
    dependencia: "Municipal (SLEP / CMDS)",
    sncae: "Sin Certificación",
    docente: "Equipo Docente Línea Azul",
    n_evals: 14,
    pre_norm5: 1.83,
    post_norm5: 3.19,
    delta_norm5: 1.37,
    pct_fav: 85.7,
    mej: 11,
    man: 1,
    ret: 2,
    hake: 0.373,
    climaton: "No participó en Climatón",
    recomendaciones: "Salto conceptual notable (+1.37 pts). Para los estudiantes con dudas en Desierto Azul, repasar la distinción entre basura biodegradable y no biodegradable (plásticos y filtros de cigarro)."
  },
  "Escuela Juan Pablo II": {
    dependencia: "Municipal (SLEP / CMDS)",
    sncae: "Sin Certificación",
    docente: "Equipo Docente Línea Azul",
    n_evals: 17,
    pre_norm5: 2.36,
    post_norm5: 3.64,
    delta_norm5: 1.27,
    pct_fav: 100.0,
    mej: 14,
    man: 3,
    ret: 0,
    hake: 0.536,
    climaton: "No participó en Climatón",
    recomendaciones: "Líder regional en Ganancia de Hake (G = 0.536). El 100% de los casos analizados fue favorable. Se aconseja vincular este aprendizaje con el comité ambiental para postular al SNCAE."
  },
  "Escuela República de Estados Unidos": {
    dependencia: "Municipal (SLEP / CMDS)",
    sncae: "Sin Certificación",
    docente: "Equipo Docente Línea Azul",
    n_evals: 17,
    pre_norm5: 2.65,
    post_norm5: 3.60,
    delta_norm5: 0.95,
    pct_fav: 94.1,
    mej: 11,
    man: 5,
    ret: 1,
    hake: 0.400,
    climaton: "9 estudiantes evaluados (100% favorable)",
    recomendaciones: "Excelente retención conceptual (94.1% favorable). Destacaron por su activa participación en Climatón formulando soluciones creativas para el reciclaje de colillas costeras."
  },
  "Escuela República de Italia": {
    dependencia: "Municipal (SLEP / CMDS)",
    sncae: "Sin Certificación",
    docente: "Equipo Docente Línea Azul",
    n_evals: 19,
    pre_norm5: 2.22,
    post_norm5: 3.00,
    delta_norm5: 0.79,
    pct_fav: 89.5,
    mej: 10,
    man: 7,
    ret: 2,
    hake: 0.316,
    climaton: "8 estudiantes evaluados (100% favorable)",
    recomendaciones: "Cohorte numerosa y entusiasta (19 evaluaciones). Para consolidar, reforzar el rol de los tiburones tollo como especies pacíficas que regulan la sobrepoblación de peces enfermos."
  },
  "Liceo Domingo Herrera Rivera": {
    dependencia: "Municipal (SLEP / CMDS)",
    sncae: "Sin Certificación",
    docente: "Equipo Docente Línea Azul",
    n_evals: 16,
    pre_norm5: 2.34,
    post_norm5: 3.32,
    delta_norm5: 0.97,
    pct_fav: 87.5,
    mej: 13,
    man: 1,
    ret: 2,
    hake: 0.418,
    climaton: "8 estudiantes evaluados (100% favorable)",
    recomendaciones: "Rendimiento muy positivo con G = 0.418. Se recomienda formalizar un taller extracurricular de monitoreo ciudadano de playas para aprovechar la motivación de los estudiantes."
  }
};

// Document Ready
document.addEventListener('DOMContentLoaded', async () => {
  await loadData();
  populateSchoolFilter();
  renderKpis();
  renderCharts();
  renderSchoolsTable();
  renderSchoolsCards();
  if (window.lucide) {
    lucide.createIcons();
  }
});

async function loadData() {
  try {
    const res = await fetch('data.json');
    if (res.ok) {
      RAW_DATA = await res.json();
      console.log('data.json cargado exitosamente.');
    } else {
      throw new Error('Respuesta de red no válida');
    }
  } catch (e) {
    console.warn('Cargando con datos fallback locales:', e);
    RAW_DATA = EMBEDDED_FALLBACK;
  }
  updateSyncBadge();
}

function updateSyncBadge() {
  const syncText = document.getElementById('sync-text');
  if (syncText) {
    syncText.textContent = `Línea Azul: 132 Eval. Normalizadas (0-5.0)`;
  }
}

// Tab Switching
function switchTab(tabId) {
  ACTIVE_TAB = tabId;
  document.querySelectorAll('.tab-view').forEach(el => el.classList.add('hidden'));
  document.querySelectorAll('.nav-tab').forEach(el => {
    el.classList.remove('active-tab', 'bg-[#0284c7]', 'text-white');
    el.classList.add('text-slate-600', 'hover:text-slate-900', 'hover:bg-slate-100');
  });

  const targetView = document.getElementById(`view-${tabId}`);
  const targetBtn = document.getElementById(`tab-btn-${tabId}`);
  if (targetView) targetView.classList.remove('hidden');
  if (targetBtn) {
    targetBtn.classList.add('active-tab', 'bg-[#0284c7]', 'text-white');
    targetBtn.classList.remove('text-slate-600', 'hover:text-slate-900', 'hover:bg-slate-100');
  }

  // Hide or show top filters if needed
  const filtersContainer = document.getElementById('filters-container');
  if (filtersContainer) {
    filtersContainer.style.display = (tabId === 'resumen') ? 'flex' : 'none';
  }

  if (window.lucide) lucide.createIcons();
}

// Scope Hito Switching
function setHito(hito) {
  CURRENT_HITO = hito;
  const btnGlobal = document.getElementById('btn-hito-global');
  const btnChallwa = document.getElementById('btn-hito-challwa');
  const btnDesierto = document.getElementById('btn-hito-desierto');

  [btnGlobal, btnChallwa, btnDesierto].forEach(btn => {
    if (btn) {
      btn.className = "px-4 py-1.5 rounded-full text-xs font-medium text-slate-600 hover:text-slate-900 transition";
    }
  });

  const activeBtn = hito === 'Global' ? btnGlobal : (hito === 'Challwa' ? btnChallwa : btnDesierto);
  if (activeBtn) {
    activeBtn.className = "px-4 py-1.5 rounded-full text-xs font-bold bg-[#0284c7] text-white shadow-sm transition";
  }

  updateHitoBanner();
  renderKpis();
  renderCharts();
  applyFilters();
}

function updateHitoBanner() {
  const title = document.getElementById('banner-title');
  const desc = document.getElementById('banner-desc');
  const sample = document.getElementById('banner-sample-text');

  if (CURRENT_HITO === 'Global') {
    if (title) title.textContent = "Resumen Global del Aprendizaje (Hito 3 + Hito 4)";
    if (desc) desc.textContent = "Evaluación consolidada en escala normalizada 0 a 5.0 puntos. Integra el reconocimiento ecológico de tiburones, rayas y biodiversidad marina (Hito 3: «El litoral que nadie conoce») con la concientización sobre plásticos y colillas costeras (Hito 4: «El plástico que viajó desde el desierto»).";
    if (sample) sample.textContent = "Muestra: 132 evaluaciones pareadas (76 estudiantes únicos en 8 colegios)";
  } else if (CURRENT_HITO === 'Challwa') {
    if (title) title.textContent = "Hito 3: «El litoral que nadie conoce» · Biodiversidad Marina y Condrictios";
    if (desc) desc.textContent = "Evaluación centrada en la trama trófica del océano de Antofagasta, identificación de especies locales (tiburón tollo, gatopardo, raya águila, pez guitarra) y su rol regulador frente a presas y lobos marinos.";
    if (sample) sample.textContent = "Muestra Hito 3: 67 evaluaciones pareadas (8 colegios)";
  } else {
    if (title) title.textContent = "Hito 4: «El plástico que viajó desde el desierto» · Plásticos y Conservación Litoral";
    if (desc) desc.textContent = "Evaluación focalizada en vectores de contaminación litoral, tiempo de degradación de materiales y el reconocimiento de las colillas de cigarro como el residuo más tóxico y numeroso de las playas.";
    if (sample) sample.textContent = "Muestra Hito 4: 65 evaluaciones pareadas (8 colegios)";
  }
}

function toggleCompareMode() {
  const section = document.getElementById('section-comparativa');
  if (section) {
    section.scrollIntoView({ behavior: 'smooth' });
    section.classList.add('ring-4', 'ring-sky-400', 'transition', 'duration-500');
    setTimeout(() => {
      section.classList.remove('ring-4', 'ring-sky-400');
    }, 2000);
  }
}

// KPI Rendering
function renderKpis() {
  const res = RAW_DATA.resumen_linea_azul;
  let pctFav = 0, countFav = "", postVal = "", postPct = "", hakeVal = "", deltaVal = "", deltaPct = "";

  if (CURRENT_HITO === 'Global') {
    pctFav = res.tasa_favorable_global;
    countFav = `${res.mejoraron_global + res.mantuvieron_global} de ${res.total_evaluaciones_pareadas} favorables`;
    postVal = `${res.puntaje_post_norm5} <span class="text-xs font-normal text-slate-400">/ 5.0</span>`;
    postPct = `${Math.round(res.puntaje_post_norm5 / 5 * 100)}% logro conceptual`;
    hakeVal = `+${res.hake_global}`;
    deltaVal = `+${res.delta_norm5}`;
    deltaPct = `+${Math.round(res.delta_norm5 / 5 * 100)}% avance neto`;
  } else if (CURRENT_HITO === 'Challwa') {
    const ch = res.challwa;
    pctFav = ch.tasa_favorable;
    countFav = `${ch.mejoraron + ch.mantuvieron} de ${ch.n} favorables`;
    postVal = `${ch.post_norm5} <span class="text-xs font-normal text-slate-400">/ 5.0</span>`;
    postPct = `${Math.round(ch.post_norm5 / 5 * 100)}% (${ch.post_raw_9}/9 pts raw)`;
    hakeVal = `+${ch.hake}`;
    deltaVal = `+${ch.delta_norm5}`;
    deltaPct = `+${Math.round(ch.delta_norm5 / 5 * 100)}% (+${(ch.post_raw_9 - ch.pre_raw_9).toFixed(1)} raw)`;
  } else {
    const da = res.desierto_azul;
    pctFav = da.tasa_favorable;
    countFav = `${da.mejoraron + da.mantuvieron} de ${da.n} favorables`;
    postVal = `${da.post_norm5} <span class="text-xs font-normal text-slate-400">/ 5.0</span>`;
    postPct = `${Math.round(da.post_norm5 / 5 * 100)}% (${da.post_raw_4}/4 pts raw)`;
    hakeVal = `+${da.hake}`;
    deltaVal = `+${da.delta_norm5}`;
    deltaPct = `+${Math.round(da.delta_norm5 / 5 * 100)}% (+${(da.post_raw_4 - da.pre_raw_4).toFixed(2)} raw)`;
  }

  setElText('kpi-pct-favorable', `${pctFav}%`);
  setElText('kpi-count-favorable', countFav);
  const postEl = document.getElementById('kpi-post');
  if (postEl) postEl.innerHTML = postVal;
  setElText('kpi-post-detail', postPct);
  setElText('kpi-hake-val', `G = ${hakeVal}`);
  setElText('kpi-hake-card', hakeVal);
  setElText('kpi-delta', deltaVal);
  setElText('kpi-delta-detail', deltaPct);
}

function setElText(id, text) {
  const el = document.getElementById(id);
  if (el) el.textContent = text;
}

// Chart.js Rendering
function renderCharts() {
  renderDonutChart();
  renderQuestionsChart();
  renderSchoolsDeltaChart();
  renderComparisonPacChart();
}

function renderDonutChart() {
  const ctx = document.getElementById('chart-status-donut');
  if (!ctx) return;
  if (CHARTS['donut']) CHARTS['donut'].destroy();

  const res = RAW_DATA.resumen_linea_azul;
  let mej = 0, man = 0, ret = 0;

  if (CURRENT_HITO === 'Global') {
    mej = res.mejoraron_global;
    man = res.mantuvieron_global;
    ret = res.retrocedieron_global;
  } else if (CURRENT_HITO === 'Challwa') {
    mej = res.challwa.mejoraron;
    man = res.challwa.mantuvieron;
    ret = res.challwa.retrocedieron;
  } else {
    mej = res.desierto_azul.mejoraron;
    man = res.desierto_azul.mantuvieron;
    ret = res.desierto_azul.retrocedieron;
  }

  const total = mej + man + ret;
  setElText('leg-mej', `${mej}`);
  setElText('leg-man', `${man}`);
  setElText('leg-ret', `${ret}`);

  CHARTS['donut'] = new Chart(ctx, {
    type: 'doughnut',
    data: {
      labels: ['Mejoró (+pts)', 'Mantuvo (0 pts)', 'Requiere Refuerzo (-pts)'],
      datasets: [{
        data: [mej, man, ret],
        backgroundColor: ['#10b981', '#0ea5e9', '#f59e0b'],
        borderWidth: 2,
        borderColor: '#ffffff'
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: { display: false },
        tooltip: {
          callbacks: {
            label: (item) => ` ${item.label}: ${item.raw} (${((item.raw / total) * 100).toFixed(1)}%)`
          }
        }
      },
      cutout: '72%'
    }
  });
}

function renderQuestionsChart() {
  const ctx = document.getElementById('chart-questions-bar');
  if (!ctx) return;
  if (CHARTS['questions']) CHARTS['questions'].destroy();

  let labels = [], preData = [], postData = [];

  if (CURRENT_HITO === 'Global' || CURRENT_HITO === 'Challwa') {
    const qCh = RAW_DATA.resumen_linea_azul.challwa.preguntas;
    labels = qCh.map(q => q.enunciado);
    preData = qCh.map(q => q.pre_pct);
    postData = qCh.map(q => q.post_pct);
    if (CURRENT_HITO === 'Global') {
      const qDa = RAW_DATA.resumen_linea_azul.desierto_azul.preguntas;
      labels = labels.concat(qDa.map(q => q.enunciado));
      preData = preData.concat(qDa.map(q => q.pre_pct));
      postData = postData.concat(qDa.map(q => q.post_pct));
    }
  } else {
    const qDa = RAW_DATA.resumen_linea_azul.desierto_azul.preguntas;
    labels = qDa.map(q => q.enunciado);
    preData = qDa.map(q => q.pre_pct);
    postData = qDa.map(q => q.post_pct);
  }

  CHARTS['questions'] = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: labels.map(l => l.length > 28 ? l.substring(0, 26) + '...' : l),
      datasets: [
        {
          label: 'Diagnóstico Inicial (PRE)',
          data: preData,
          backgroundColor: '#94a3b8',
          borderRadius: 6
        },
        {
          label: 'Evaluación de Cierre (POST)',
          data: postData,
          backgroundColor: '#0284c7',
          borderRadius: 6
        }
      ]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      scales: {
        y: {
          beginAtZero: true,
          max: 100,
          ticks: { callback: v => v + '%' }
        },
        x: {
          ticks: { font: { size: 10 } }
        }
      },
      plugins: {
        legend: { position: 'top', labels: { boxWidth: 12, font: { size: 11 } } },
        tooltip: {
          callbacks: {
            label: (item) => ` ${item.dataset.label}: ${item.raw.toFixed(1)}%`
          }
        }
      }
    }
  });
}

function renderSchoolsDeltaChart() {
  const ctx = document.getElementById('chart-schools-delta');
  if (!ctx) return;
  if (CHARTS['schoolsDelta']) CHARTS['schoolsDelta'].destroy();

  const schoolNames = Object.keys(SCHOOLS_DIRECTORY);
  const deltas = schoolNames.map(s => SCHOOLS_DIRECTORY[s].delta_norm5);
  const hakes = schoolNames.map(s => SCHOOLS_DIRECTORY[s].hake);

  // Short labels
  const shortNames = schoolNames.map(s => {
    return s.replace('Escuela Ecológica ', 'Esc. ')
            .replace('Escuela República de ', 'Esc. Rep. ')
            .replace('Escuela ', 'Esc. ')
            .replace('Liceo ', 'Lic. ');
  });

  CHARTS['schoolsDelta'] = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: shortNames,
      datasets: [
        {
          label: 'Delta Promedio (POST - PRE)',
          data: deltas,
          backgroundColor: deltas.map(d => d >= 1.0 ? '#0284c7' : (d >= 0.5 ? '#38bdf8' : '#7dd3fc')),
          borderRadius: 6
        }
      ]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      scales: {
        y: {
          beginAtZero: true,
          title: { display: true, text: 'Puntos de Avance (Escala 0-5.0)' }
        },
        x: {
          ticks: { font: { size: 9 }, maxRotation: 45 }
        }
      },
      plugins: {
        legend: { display: false },
        tooltip: {
          callbacks: {
            title: (items) => schoolNames[items[0].dataIndex],
            label: (item) => ` Delta: +${item.raw.toFixed(2)} pts | Hake G: ${hakes[item.dataIndex]}`
          }
        }
      }
    }
  });
}

function renderComparisonPacChart() {
  const ctx = document.getElementById('chart-comparison-pac');
  if (!ctx) return;
  if (CHARTS['comparisonPac']) CHARTS['comparisonPac'].destroy();

  const comp = RAW_DATA.comparativa_lineas;

  CHARTS['comparisonPac'] = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ['Línea Verde (7 Escuelas)', 'Línea Azul (8 Escuelas)', 'Consolidado PAC 2026 (15 Escuelas)'],
      datasets: [
        {
          label: 'Puntaje PRE (Norm. 0-5)',
          data: [comp.linea_verde.pre_promedio_norm5, comp.linea_azul.pre_promedio_norm5, comp.total_pac_consolidado.pre_promedio_norm5],
          backgroundColor: 'rgba(148, 163, 184, 0.6)',
          borderRadius: 6
        },
        {
          label: 'Puntaje POST (Norm. 0-5)',
          data: [comp.linea_verde.post_promedio_norm5, comp.linea_azul.post_promedio_norm5, comp.total_pac_consolidado.post_promedio_norm5],
          backgroundColor: ['#10b981', '#0ea5e9', '#6366f1'],
          borderRadius: 6
        },
        {
          label: 'Tasa Favorable (%)',
          data: [comp.linea_verde.tasa_favorable_global, comp.linea_azul.tasa_favorable_global, comp.total_pac_consolidado.tasa_favorable_ponderada],
          type: 'line',
          borderColor: '#f59e0b',
          backgroundColor: '#f59e0b',
          yAxisID: 'y1',
          borderWidth: 3,
          pointRadius: 5
        }
      ]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      scales: {
        y: {
          beginAtZero: true,
          max: 5.0,
          title: { display: true, text: 'Puntaje (0 a 5.0)', color: '#cbd5e1' },
          grid: { color: 'rgba(255, 255, 255, 0.1)' },
          ticks: { color: '#cbd5e1' }
        },
        y1: {
          position: 'right',
          beginAtZero: false,
          min: 60,
          max: 100,
          title: { display: true, text: '% Tasa Favorable', color: '#f59e0b' },
          grid: { display: false },
          ticks: { callback: v => v + '%', color: '#f59e0b' }
        },
        x: {
          ticks: { color: '#e2e8f0', font: { weight: 'bold' } },
          grid: { color: 'rgba(255, 255, 255, 0.05)' }
        }
      },
      plugins: {
        legend: {
          position: 'top',
          labels: { color: '#e2e8f0', boxWidth: 12 }
        }
      }
    }
  });
}

// Schools Table Rendering
function renderSchoolsTable() {
  const tbody = document.getElementById('schools-table-body');
  if (!tbody) return;
  tbody.innerHTML = '';

  Object.entries(SCHOOLS_DIRECTORY).forEach(([name, data]) => {
    const isSncae = data.sncae.includes('Sello') || data.sncae.includes('Certificación');
    const sncaeBadge = isSncae 
      ? `<span class="px-2.5 py-0.5 rounded-full text-[10px] font-extrabold bg-sky-100 text-[#0369a1] border border-sky-300">Sello Ambiental</span>`
      : `<span class="px-2.5 py-0.5 rounded-full text-[10px] font-medium bg-slate-100 text-slate-500 border border-slate-200">Sin SNCAE</span>`;

    const row = document.createElement('tr');
    row.className = "hover:bg-slate-50/80 transition school-row";
    row.dataset.school = name;

    row.innerHTML = `
      <td class="py-3 px-4 font-bold text-slate-900">${name}</td>
      <td class="py-3 px-3 text-slate-600">${data.dependencia}</td>
      <td class="py-3 px-3">${sncaeBadge}</td>
      <td class="py-3 px-3 text-center font-bold text-slate-800">${data.n_evals}</td>
      <td class="py-3 px-3 text-center text-slate-600 font-medium">${data.pre_norm5.toFixed(2)}</td>
      <td class="py-3 px-3 text-center font-extrabold text-emerald-700">${data.post_norm5.toFixed(2)}</td>
      <td class="py-3 px-3 text-center font-extrabold text-sky-700">+${data.delta_norm5.toFixed(2)}</td>
      <td class="py-3 px-3 text-center">
        <span class="px-2.5 py-1 rounded-full text-xs font-black ${data.pct_fav >= 90 ? 'bg-emerald-100 text-emerald-800' : 'bg-sky-100 text-sky-800'}">
          ${data.pct_fav.toFixed(1)}%
        </span>
      </td>
      <td class="py-3 px-3">
        <div class="flex items-center gap-1 w-24">
          <div class="h-2 rounded-l-full bg-emerald-500" style="width: ${(data.mej / data.n_evals) * 100}%" title="Mejoraron: ${data.mej}"></div>
          <div class="h-2 bg-sky-400" style="width: ${(data.man / data.n_evals) * 100}%" title="Mantuvieron: ${data.man}"></div>
          <div class="h-2 rounded-r-full bg-amber-400" style="width: ${(data.ret / data.n_evals) * 100}%" title="Refuerzo: ${data.ret}"></div>
        </div>
      </td>
      <td class="py-3 px-4 text-center">
        <span class="text-[11px] font-semibold text-slate-600">${data.climaton.split(' ')[0]} est.</span>
      </td>
    `;
    tbody.appendChild(row);
  });
}

function renderSchoolsCards() {
  const container = document.getElementById('schools-cards-container');
  if (!container) return;
  container.innerHTML = '';

  Object.entries(SCHOOLS_DIRECTORY).forEach(([name, data]) => {
    const card = document.createElement('div');
    card.className = "p-5 rounded-2xl bg-white border border-slate-200 card-shadow space-y-3";
    card.innerHTML = `
      <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-100 pb-3">
        <div>
          <h4 class="text-base font-extrabold text-slate-900">${name}</h4>
          <span class="text-xs text-slate-500">${data.dependencia} • ${data.sncae}</span>
        </div>
        <div class="flex items-center gap-2">
          <span class="px-3 py-1 rounded-full text-xs font-black bg-sky-50 text-[#0284c7] border border-sky-200">
            Tasa Favorable: ${data.pct_fav.toFixed(1)}% (${data.mej + data.man}/${data.n_evals})
          </span>
          <span class="px-3 py-1 rounded-full text-xs font-bold bg-emerald-50 text-emerald-800 border border-emerald-200">
            Hake G: ${data.hake}
          </span>
        </div>
      </div>
      <div class="grid grid-cols-1 md:grid-cols-4 gap-4 text-xs">
        <div class="p-3 rounded-xl bg-slate-50 border border-slate-100">
          <span class="text-slate-400 block font-semibold">Diagnóstico Inicial (PRE)</span>
          <strong class="text-slate-800 text-sm">${data.pre_norm5.toFixed(2)} / 5.0 pts</strong>
        </div>
        <div class="p-3 rounded-xl bg-slate-50 border border-slate-100">
          <span class="text-slate-400 block font-semibold">Cierre Formativo (POST)</span>
          <strong class="text-emerald-700 text-sm">${data.post_norm5.toFixed(2)} / 5.0 pts</strong>
        </div>
        <div class="p-3 rounded-xl bg-slate-50 border border-slate-100">
          <span class="text-slate-400 block font-semibold">Avance Neto (Delta)</span>
          <strong class="text-sky-700 text-sm">+${data.delta_norm5.toFixed(2)} pts (+${Math.round(data.delta_norm5 / 5 * 100)}%)</strong>
        </div>
        <div class="p-3 rounded-xl bg-slate-50 border border-slate-100">
          <span class="text-slate-400 block font-semibold">Participación Climatón</span>
          <strong class="text-amber-700 text-sm">${data.climaton}</strong>
        </div>
      </div>
      <div class="p-3 rounded-xl bg-sky-50/50 border border-sky-100 text-xs">
        <strong class="text-[#0369a1] block mb-1 flex items-center gap-1.5">
          <i data-lucide="compass" class="w-3.5 h-3.5"></i>
          Orientación Pedagógica para Profesor/a Líder:
        </strong>
        <p class="text-slate-700 leading-relaxed">${data.recomendaciones}</p>
      </div>
    `;
    container.appendChild(card);
  });
}

function populateSchoolFilter() {
  const select = document.getElementById('filter-school');
  if (!select) return;
  Object.keys(SCHOOLS_DIRECTORY).forEach(s => {
    const opt = document.createElement('option');
    opt.value = s;
    opt.textContent = s;
    select.appendChild(opt);
  });
}

function applyFilters() {
  const school = document.getElementById('filter-school')?.value || 'ALL';
  const status = document.getElementById('filter-status')?.value || 'ALL';
  const search = document.getElementById('filter-search')?.value.toLowerCase().trim() || '';

  // Filter school rows in table
  document.querySelectorAll('.school-row').forEach(row => {
    const sName = row.dataset.school;
    const matchSchool = (school === 'ALL' || sName === school);
    const matchSearch = (!search || sName.toLowerCase().includes(search));
    row.style.display = (matchSchool && matchSearch) ? '' : 'none';
  });
}

function exportSchoolsTable() {
  let csv = "Establecimiento,Dependencia,Acreditacion_SNCAE,Evaluaciones,PRE_Norm,POST_Norm,Delta_Norm,Tasa_Favorable_Pct,Hake_G\n";
  Object.entries(SCHOOLS_DIRECTORY).forEach(([name, d]) => {
    csv += `"${name}","${d.dependencia}","${d.sncae}",${d.n_evals},${d.pre_norm5},${d.post_norm5},${d.delta_norm5},${d.pct_fav},${d.hake}\n`;
  });

  const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = `Reporte_Línea_Azul_PAC2026_${new Date().toISOString().slice(0, 10)}.csv`;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
}
