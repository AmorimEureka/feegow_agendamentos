
SELECT
    a.agendamento_id,
    a.unidade_id,
    a.local_id,
    a.paciente_id,
    a.procedimento_id,
    a.especialidade_id,
    a.profissional_id,
    a.status_id,
    a.data,
    a.horario,
    a.agendado_em,
    a.primeiro_agendamento,
    a.encaixe,
    a.telemedicina
FROM raw_feegow.agendamentos a
LIMIT 10
;

SELECT
    c.id,
    c.canal
FROM raw_feegow.canais c
;
