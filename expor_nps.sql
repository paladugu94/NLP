create table nps_2019_2020 as
select *
from marketing.tnps_datos
where response_date >= to_date('01/01/2019','dd/mm/yyyy')--cambiar por la fecha solicitada
and survey_status_analysis ='Completed'
and tnps_score is not null
and tnps_comment is not null
order by response_date asc;

--creo una tabla ordenada por case_number,feedback_call_time
create table nps_2019_2020_2 as
select /*+ parallel(a,10)*/distinct * from nps_2019_2020 a
order by case_number,feedback_call_time desc

--crei el index
create index DERT432WED on NPS_2019_2020_2 (CASE_NUMBER)
--agrego el campo paea desduplicar
alter table nps_2019_2020_2 add mca_dupli varchar2(12);

--proceso para desduplicar
BEGIN
*
MARCA_DUPLI_NPS2;
END;

select count(case_number),count(distinct case_number) from NPS_2019_2020_2
where mca_dupli is null

